"""
This module holds server code.
"""


from typing import List
from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from src.drink import Drink

#TODO get rid of these
import json


@dataclass
class Request:
    """
    struct to hold a few attributes of a drink request
    """
    drink: Drink  # holds recipe and ID
    user_ID: str
    time: datetime
    _filled: bool
    started: bool

    def filled(self) -> float:
        """
        Whether a drink is finished. If the drink ever finds itself to be finished, a flag is set so we don't evaluate all the pours again
        :return: bool
        """
        if self._filled:
            return 1.0

        progress = self.drink.get_progress()
        if progress >= 1.0:
            self._filled = True
            return 1.0

        return progress


_drink_requests: List[Request] = list()  # holds requests, sorted in time order. They are generated in time order so no sorting needed


# Private functions


def _make_request(recipe_str: str, user_ID: str, time: datetime) -> Request:
    """
    generates a request object
    :param recipe_str: the recipe string to make
    :param time: time the req was received
    :return: initialized Request Object
    """
    return Request(
        drink=Drink(recipe_str),
        user_ID=user_ID,
        time=time,
        _filled=False,
        started=False
    )


def _parse_server_request(req_str: str) -> Request:
    """
    parses raw input from server request
    :param req_str:
    :return:
    """
    #TODO figure out server request format; implement


# Public Functions

calls: int = 0

def update():
    """
    updates server handler business
    * gets requests
    * updates lists of requests and their filled states
    :return: None
    """

    # TODO make this for real and not fake
    global calls
    calls += 1

    if calls == 5:
        with open("sample_data/example_recipes.json") as file:
            recipe_list = json.loads(file.read())
        _drink_requests.append(_make_request(json.dumps(recipe_list[0]), 'bennett', datetime.now()))
        print('Server: got drink request: {}'.format(_drink_requests[0]))


def has_drink_request() -> bool:
    """
    Whether there is a drink request to be filled
    :return: bool
    """

    for drink_req in _drink_requests:
        if drink_req.started:
            continue

        return True


def get_next_drink() -> Drink:
    """
    Gets next drink from unfilled request in req list.
    :return: Drink
    """

    for drink_req in _drink_requests:
        if drink_req.started:
            continue

        drink_req.started = True
        return drink_req.drink


def get_drink_status(_id: UUID) -> float:
    """
    Gets the status of
    :param _id: the UUId of the drink to check on
    :return: float btwn 0 and 1. 0 is not started, 1 is done.
    """

    for drink_req in _drink_requests:
        if not drink_req.drink.ID == _id:
            continue

        return drink_req.filled()


from time import sleep, perf_counter

from src.pour import waiting_for_pours, start_all_pours, update_all_pours
from src.drink import add_drink_pours
from src import server
from src.sensor import ready_to_pour, set_pour_ready_sensor, Always_1_Sensor
from src.solenoid import add_solenoid, Console_Solenoid


MAX_LOOPS_PER_SEC: int = 2


def init():
    """
    runs on startup. starts server, initializes sensors and solenoids, etc.
    :return:
    """

    # Initialize solenoids
    add_solenoid(Console_Solenoid('VODKA'), 'VODKA')
    add_solenoid(Console_Solenoid('FRUIT_PUNCH'), 'FRUIT_PUNCH')

    # Initialize sensors
    set_pour_ready_sensor(Always_1_Sensor())


# TODO remove print statements
def loop():
    """
    main loop on control board. performs tasks:
    * check server for requests in threadsafe data structure
    :return: None
    """
    print('Main: looping...')

    # refresh server
    server.update()

    # If we have a drink request and are ready to start working on the next drink, start that
    if server.has_drink_request() and waiting_for_pours():
        print('Main: adding pours')
        add_drink_pours(server.get_next_drink())

    # If there are pours ready and the machine is ready to pour, start pouring
    if not waiting_for_pours() and ready_to_pour():
        print('Main: starting pours')
        start_all_pours()

    # Update pour objects
    update_all_pours()



def main():
    init()

    goal_loop_dtm = 1.0 / MAX_LOOPS_PER_SEC
    loop_start_time = None

    while True:
        loop_start_time = perf_counter()
        loop()

        # figure out how long to wait for next iter
        last_loop_dtm = perf_counter() - loop_start_time
        wait_time = max(0.0, goal_loop_dtm - last_loop_dtm)

        # wait
        sleep(wait_time)


if __name__ == '__main__':
    main()
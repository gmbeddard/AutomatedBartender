from time import perf_counter  # timer fn

from pour import Pour

POUR_RATE = 0.8

class Timed_Pour(Pour):
    """
    Pour for time. uses no sensors. uses final float POUR_RATE to determine amount/time

    This is a 'default' implementation I am designing, probably wont be used.
    """

    start_tm: float

    def __init__(self):
        super().__init__()

    def start_pour(self):
        super()  # Opens solenoid
        self.start_tm = perf_counter()

    def update(self):
        if not self.is_pouring():
            return

        self.current_amount = (perf_counter() - self.start_tm) * POUR_RATE
        if self.current_amount >= self.recipe_amount:
            self.stop_pour()

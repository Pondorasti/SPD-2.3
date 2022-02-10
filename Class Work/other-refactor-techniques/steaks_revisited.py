# by Kami Bigdely
# Extract class
WELL_DONE = 3000
MEDIUM = 2500
COOKED_CONSTANT = 0.05


class Steak:
    def __init__(self, time, temp, pressure, desired_state):
        self.time = time
        self.temp = temp
        self.pressure = pressure
        self.desired_state = desired_state

    def __is_cookeding_criteria_satisfied(self):
        return self.__is_well_done() or self.__is_medium()

    def __is_well_done(self):
        return self.desired_state == 'well-done' and self.__get_cooking_progress() >= WELL_DONE

    def __is_medium(self):
        return self.desired_state == 'medium' and self.__get_cooking_progress() >= MEDIUM

    def __get_cooking_progress(self):
        return self.time * self.temp * self.pressure * COOKED_CONSTANT

    def __str__(self):
        if self.__is_cookeding_criteria_satisfied():
            return 'Cooking progress: done'
        return "Cooking progress: ongoing"


time = 30  # [min]
temp = 103  # [celcius]
pressure = 20  # [psi]
desired_state = 'well-done'

steak = Steak(time, temp, pressure, desired_state)
print(steak)

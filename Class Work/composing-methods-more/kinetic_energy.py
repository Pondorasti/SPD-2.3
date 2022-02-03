# By Kami Bigdely
# Remove assignment to method parameter.

class Distance:
    def __init__(self, value, unit):
        self.unit = unit
        self.value = value


class Mass:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit


def calculate_kinetic_energy(mass, distance, time):
    adjusted_distance = 0
    if distance.unit != 'km':
        # [ly] stands for light-year (measure of distance in astronomy)
        if distance.unit == "ly":
            # convert from light-year to km unit
            adjusted_distance = distance.value * 9.461e12
        else:
            print("unit is Unknown")
            return

    adjusted_mass = 0
    if mass.unit != 'kg':
        if mass.unit == "solar-mass":
            # convert from solar mass to kg
            adjusted_mass = mass.value * 1.98892e30
        else:
            print("unit is Unknown")
            return

    speed = adjusted_distance / time  # [km per sec]
    kinetic_energy = 0.5 * adjusted_mass * speed ** 2
    return kinetic_energy


mass = Mass(2, "solar-mass")
distance = Distance(2, 'ly')
print(calculate_kinetic_energy(mass, distance, 3600e20))

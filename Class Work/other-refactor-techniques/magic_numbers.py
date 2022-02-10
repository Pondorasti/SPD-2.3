# by Kami Bigdely
# Replace magic numbers with named constanst

COULOMB_CONSTANT = 8.9875517923*1e9
EVEN_CONSTANT = 2

# First Section


def electric_force(charge1, charge2, distance):
    return COULOMB_CONSTANT * (charge1 * charge2) / distance**2


q1 = int(input('Enter a value of charge q1: '))
q2 = int(input('Enter a value of charge q2: '))
distance = int(input("Enter the distance be10tween two charges: "))
print("Electric Force between q1 and q2 is: ",
      electric_force(q1, q2, distance), "Newton")

# Second Section


def is_even(number):
    return number % EVEN_CONSTANT == 0


num = int(input('Enter an integer number: '))
if is_even(num):
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")

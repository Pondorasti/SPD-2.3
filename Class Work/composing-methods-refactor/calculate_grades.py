# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.

import math


def calculate_mean(scores):
    total = 0
    for score in scores:
        total += score
    return total / len(scores)


def calculate_standard_deviation(scores, mean):
    sum_of_sqrs = 0
    for score in scores:
        sum_of_sqrs += (score - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(scores))
    return sd


def print_stat():
    grade_list = []

    # Get the inputs from the user
    n_student = 5
    for _ in range(n_student):
        grade_list.append(int(input('Enter a number: ')))

    # Calculate the mean and standard deviation of the grades
    mean = calculate_mean(grade_list)
    sd = calculate_standard_deviation(grade_list, mean)

    # print out the mean and standard deviation in a nice format.
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')


print_stat()

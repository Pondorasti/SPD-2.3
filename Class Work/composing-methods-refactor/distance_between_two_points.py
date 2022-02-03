# Written by Kamran Bigdely

import math

xc1 = 4
yc1 = 4.25

xc2 = 53
yc2 = -5.35


def distance_between_two_points(x1, y1, x2, y2):
    '''Calculate the distance between the two points.'''
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distance


print('distance', distance_between_two_points(xc1, yc1, xc2, yc2))


# =======================

xa = -36
ya = 97

xb = .34
yb = .91


def vector_length(xa, ya, xb, yb):
    '''Calculate the length of vector AB.'''
    length = distance_between_two_points(xa, ya, xb, yb)
    return length


print('length', vector_length(xa, ya, xb, yb))

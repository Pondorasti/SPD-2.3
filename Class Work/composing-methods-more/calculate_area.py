# by Kami Bigdely
# Rename Method
# Reference: https://parade.com/1039985/marynliles/pick-up-lines/

def cal_area_under_graph(graph):
    """Calculate the area under the input graph."""
    pass

#####################


def find_biggest_value(li):
    m = li[0]
    for value in li:
        if value > m:
            m = value
    return m


li = [5, -1, 43, 32, 87, -100]
print(find_biggest_value(li))

############################


def split_whitespaces(sentence):
    words = sentence[0:].split(' ')
    return words


print(process('If you were a vegetable, you’d be a ‘cute-cumber.'))

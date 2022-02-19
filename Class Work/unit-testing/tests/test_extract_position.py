from extract_position import extract_position


def test_extract_position():
    assert extract_position(
        '|error| numerical calculations could not converge.') == None
    assert extract_position(
        '|update| the positron location in the particle accelerator is x:21.432') == "21.432"

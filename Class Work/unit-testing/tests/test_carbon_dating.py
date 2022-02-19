from carbon_dating import get_age_carbon_14_dating


def test_age_carbon():
    assert get_age_carbon_14_dating(0.35) == 8680.34743633106
    assert get_age_carbon_14_dating(0) == None
    assert get_age_carbon_14_dating(-1) == None

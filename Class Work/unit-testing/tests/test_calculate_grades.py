import pytest
from calculate_grades import calculate_stat


def test_calculate_stat():
    assert calculate_stat([1, 2, 3, 4, 5]) == (3.0, 1.4142135623730951)
    assert calculate_stat([0]) == (0.0, 0.0)

    with pytest.raises(ZeroDivisionError):
        assert calculate_stat([]) == (3.0, 1.4142135623730951)

"""Test the dedup file."""
from dedup import is_in, dedup


def test_is_in_and_dedup():
    """Test the is_in function."""
    test_list = [1, 2, 2, 3, 4, 4]
    assert is_in(test_list, 4) == True
    assert is_in(test_list, 1) == True
    assert is_in(test_list, 5) == False
    assert dedup(test_list) == [1, 2, 3, 4]

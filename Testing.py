"""Test addition."""
from add import add


def test_add():
    """Test add()."""
    assert add(1, 1) == 2
    assert add(4, 2) == 6
    assert add(17, 17) == 34

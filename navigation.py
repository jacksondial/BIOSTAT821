"""Test navigation MY CODE."""


class BadMoveError(Exception):
    """Bad move."""


def move(position: tuple[int, int], direction: str) -> tuple[int, int]:
    """Move object."""
    list_location = list(my_location)
    if direction == "north":
        list_location[1] += 1
    elif direction == "south":
        list_location[1] -= 1
    elif direction == "east":
        list_location[0] += 1
    elif direction == "west":
        list_location[0] -= 1
    else:
        raise (BadMoveError("Bad move!"))
    return tuple(list_location)


print(move((0, 0), "west"))

"""Repeat things."""


def add_1(x: int) -> int:
    """Add 1 to x."""
    return x + 1


def do_5_times(fcn):
    """Call 5 times."""

    def call_fcn(x):
        return fcn(x)

    return call_fcn


if __name__ == "__main__":
    thing = do_5_times(add_1)
    print(thing)
    print(thing(6))

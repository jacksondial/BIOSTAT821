"""Deduplication."""
from typing import TypeVar

T = TypeVar("T")


def is_in(things: list[T], target: T) -> bool:
    """Determine whether target is in things.

    O(N) total
    """
    for thing in things:  # N times
        if thing == target:
            return True
    return False


cache = dict[tuple[str], tuple[str]]


def dedup(things: list[T]) -> list[T]:
    """De-duplicate things.

    O(N**2) total
    """
    if things in cache:
        return cache[things]

    unique_things: list[T] = []
    for thing in things:  # N times
        if not is_in(unique_things, thing):  # O(N)
            unique_things.append(thing)
    cache[things] = unique_things
    return unique_things

"""Module docstring."""


# def count_paths(dict[str, list[str]], start_node: str, end_node: str)->int:
# """Docstring."""
#     i = 0
#     if end_node in start_node.values():
#         return i += 1
#     else:
#         for j in start_node.values():
#             i += (count_paths(start_node = j))
#     return i


def count_paths(
    graph: tuple[set[str], set[tuple[str, str]]], start: str, end: str
) -> int:
    """Docstring."""
    if start == end:
        return 1
    total = 0
    for edge in graph[1]:
        edge_start, edge_end = edge
        if edge_start == start:
            count_paths(graph, edge_end, end)
    return total

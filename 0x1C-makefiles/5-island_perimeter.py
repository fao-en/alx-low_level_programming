#!/usr/bin/python3
"""Function that returns the perimeter of the island."""


def island_perimeter(grid):
    """Return the perimeter of an island.

    Args:
        grid (list): A list of list of integers.
    Returns:
        The perimeter of the island defined in the grid.
    """
    rows = len(grid)
    cols = len(grid[0])
    land_count = 0
    shared_edges = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                land_count += 1
                if j > 0 and grid[i][j - 1] == 1:
                    shared_edges += 1
                if i > 0 and grid[i - 1][j] == 1:
                    shared_edges += 1
    return land_count * 4 - shared_edges * 2

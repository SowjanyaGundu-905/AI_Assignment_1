import heapq
import math


DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1),  (1, 0),  (1, 1)]

def heuristic(x, y, n):
    return math.sqrt((n-1-x)**2 + (n-1-y)**2)

def best_first_search(grid):
    n = len(grid)
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1, []

    pq = [(heuristic(0,0,n), (0,0), [(0,0)])]  
    visited = set([(0,0)])

    while pq:
        _, (x, y), path = heapq.heappop(pq)
        if (x, y) == (n-1, n-1):
            return len(path), path

        for dx, dy in DIRECTIONS:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                heapq.heappush(pq, (heuristic(nx, ny, n), (nx, ny), path+[(nx, ny)]))

    return -1, []


def a_star_search(grid):
    n = len(grid)
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1, []

    pq = [(heuristic(0,0,n), 0, (0,0), [(0,0)])]  
    visited = set()

    while pq:
        f, g, (x, y), path = heapq.heappop(pq)
        if (x, y) == (n-1, n-1):
            return len(path), path

        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in DIRECTIONS:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in visited:
                g_new = g + 1
                f_new = g_new + heuristic(nx, ny, n)
                heapq.heappush(pq, (f_new, g_new, (nx, ny), path+[(nx, ny)]))

    return -1, []


grids = [
    [[0,1],[1,0]],
    [[0,0,0],[1,1,0],[1,1,0]],
    [[1,0,0],[1,1,0],[1,1,0]]
]

for i, grid in enumerate(grids,1):
    bfs_len, bfs_path = best_first_search(grid)
    astar_len, astar_path = a_star_search(grid)
    print(f"Example {i}:")
    print(f"  Best First Search → Path length: {bfs_len}, Path: {bfs_path}")
    print(f"  A* Search        → Path length: {astar_len}, Path: {astar_path}")
    print()

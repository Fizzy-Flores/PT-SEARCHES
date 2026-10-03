import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_heap = [(heuristic(start, goal), 0, start)]
    came_from = {}
    best_g = {start: 0}

    while open_heap:
        f, g, node = heapq.heappop(open_heap)

        if node == goal:
            path = [node]
            while node in came_from:
                node = came_from[node]
                path.append(node)
            return path[::-1]

        r, c = node
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                new_g = g + 1
                if new_g < best_g.get((nr, nc), float("inf")):
                    best_g[(nr, nc)] = new_g
                    came_from[(nr, nc)] = node
                    new_f = new_g + heuristic((nr, nc), goal)
                    heapq.heappush(open_heap, (new_f, new_g, (nr, nc)))

    return None


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 0],
    ]
    print("A* path:", astar(grid, (0, 0), (3, 3)))

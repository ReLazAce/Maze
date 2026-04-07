import time
import os
from collections import deque

# Peta
maze = [
    list("##########"),
    list("#.     #E#"),
    list("# ### ## #"),
    list("#        #"),
    list("##########")
]

# Cari posisi start dan end
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == '.':
            start = (i, j)
        if maze[i][j] == 'E':
            end = (i, j)

# Arah gerak (atas, bawah, kiri, kanan)
directions = [(-1,0),(1,0),(0,-1),(0,1)]

# BFS
queue = deque([(start, [])])
visited = set()

while queue:
    (x, y), path = queue.popleft()

    if (x, y) in visited:
        continue
    visited.add((x, y))

    # Animasi
    os.system('cls' if os.name == 'nt' else 'clear')
    temp = [row[:] for row in maze]
    for px, py in path:
        temp[px][py] = '*'

    for row in temp:
        print("".join(row))

    time.sleep(0.2)

    if (x, y) == end:
        print("\nJalan ditemukan!")
        break

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if maze[nx][ny] != '#':
            queue.append(((nx, ny), path + [(nx, ny)]))
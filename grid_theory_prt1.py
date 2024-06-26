from collections import deque
from copy import deepcopy

input_file = open("input.txt", "r")
n = int(input_file.readline().strip())
grid = [list(input_file.readline().strip()) for _ in range(n)]
input_file.close()

dist = [[None for _ in range(n)] for _ in range(n)]
parent = [[None for _ in range(n)] for _ in range(n)]

# for line in grid:
#     print(repr(line))

start_row, start_col = None, None 
end_row, end_col = None, None 
for row in range(n):
    for col in range(n):
        if grid[row][col] == 'S':
            start_row, start_col = row, col
        elif grid[row][col] == 'T':
            end_row, end_col = row, col

def bfs():
    Q = deque()
    Q.append((start_row, start_col))
    dist[start_row][start_col] = 0
    while len(Q) > 0:
        row, col = Q.popleft()
        for r, c in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
            if 0 <= r < n and 0 <= c < n and grid[r][c]!= '#' and dist[r][c] is None:
                dist[r][c] = dist[row][col] + 1
                parent[r][c] = (row, col)
                Q.append((r, c))

bfs()
print(n)
route = []
end_row, end_col = parent[end_row][end_col]
while parent[end_row][end_col] is not None:
    route.append((end_row, end_col))
    end_row, end_col = parent[end_row][end_col]

output = deepcopy(grid)
for row, col in route[::-1]:
    output[row][col] = 'O'

for line in output:
    print(''.join(line))

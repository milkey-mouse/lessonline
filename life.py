#!/usr/bin/env python3
from string import ascii_uppercase

width = height = 6
board = [[0] * height for _ in range(width)]

def seed(live_cells):
    global board
    board = [[0] * height for _ in range(width)]
    for x, y in live_cells:
        if 0 <= x < width and 0 <= y < height:
            board[x][y] = 1

def step():
    global board
    new_board = [[0] * height for _ in range(width)]
    for x in range(width):
        for y in range(height):
            live_neighbors = sum(board[i][j]
                                 for i in range(x-1, x+2)
                                 for j in range(y-1, y+2)
                                 if (i != x or j != y) and 0 <= i < width and 0 <= j < height)
            if board[x][y] == 1 and live_neighbors in (2, 3):
                new_board[x][y] = 1
            elif board[x][y] == 0 and live_neighbors == 3:
                new_board[x][y] = 1
    board = new_board

def cc():
    visited = [[False] * height for _ in range(width)]

    def dfs(x, y):
        stack = [(x, y)]
        while stack:
            cx, cy = stack.pop()
            for nx, ny in ((cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1)):
                if 0 <= nx < width and 0 <= ny < height and not visited[nx][ny] and board[nx][ny]:
                    visited[nx][ny] = True
                    stack.append((nx, ny))

    connected_components = 0
    for i in range(width):
        for j in range(height):
            if board[i][j] and not visited[i][j]:
                visited[i][j] = True
                dfs(i, j)
                connected_components += 1

    return connected_components

def l():
    return sum(sum(row) for row in board)

def A():
    min_x, max_x = width, -1
    min_y, max_y = height, -1
    for i in range(width):
        for j in range(height):
            if board[i][j] == 1:
                min_x = min(min_x, i)
                max_x = max(max_x, i)
                min_y = min(min_y, j)
                max_y = max(max_y, j)
    if min_x <= max_x and min_y <= max_y:
        return (max_x - min_x + 1) * (max_y - min_y + 1)
    else:
        return 0

def longest_horizontal(t):
    max_length = 0
    for row in t:
        current_length = 0
        for cell in row:
            if cell == 1:
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                current_length = 0
    return max_length

def longest_vertical(t):
    max_length = 0
    for y in range(height):
        current_length = 0
        for x in range(width):
            if t[x][y] == 1:
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                current_length = 0
    return max_length

def longest_diagonal(t):
    max_length = 0
    for x in range(width):
        for y in range(height):
            # Diagonal down-right
            current_length = 0
            i, j = x, y
            while i < width and j < height and t[i][j] == 1:
                current_length += 1
                i += 1
                j += 1
            max_length = max(max_length, current_length)

            # Diagonal down-left
            current_length = 0
            i, j = x, y
            while i < width and j >= 0 and t[i][j] == 1:
                current_length += 1
                i += 1
                j -= 1
            max_length = max(max_length, current_length)

            # Diagonal up-right
            current_length = 0
            i, j = x, y
            while i >= 0 and j < height and t[i][j] == 1:
                current_length += 1
                i -= 1
                j += 1
            max_length = max(max_length, current_length)

            # Diagonal up-left
            current_length = 0
            i, j = x, y
            while i >= 0 and j >= 0 and t[i][j] == 1:
                current_length += 1
                i -= 1
                j -= 1
            max_length = max(max_length, current_length)

    return max_length

def s():
    return max(longest_horizontal(board), longest_vertical(board), longest_diagonal(board))

def display_with_frame():
    frame_top_bottom = '+' * (width + 2)
    print(frame_top_bottom)
    for row in board:
        print('+' + ''.join('█' if cell else ' ' for cell in row) + '+')
    print(frame_top_bottom)

seed([(1, 2), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4)])

ccl = []
ll = []
Al = []
sl = []

for t in range(1, 6):
    ccl.append(cc())
    ll.append(l())
    Al.append(A())
    sl.append(s())
    display_with_frame()
    print()
    print(f"t: {t}")
    print(f"cc: {cc()} ({ascii_uppercase[cc()]})")
    print(f"l: {l()} ({ascii_uppercase[l()]})")
    print(f"A: {A()} ({ascii_uppercase[A()]})")
    print(f"s: {s()} ({ascii_uppercase[s()]})")
    step()
    input()

print("t\t=", "\t".join(map(str, range(1, 6))))
print("l(t)\t=", "\t".join(map(str, ll)))
print("cc(t)\t=", "\t".join(map(str, ccl)))
print("A(t)\t=", "\t".join(map(str, Al)))
print("s(t)\t=", "\t".join(map(str, sl)))

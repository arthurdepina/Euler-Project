"""
In the 20 x 20 grid below, four numbers along a diagonal line
have been marked in red.
(Because this is a comment I can't highlight anything, but
the hightlighted numbers are in I-14, J-13, K-12 and L-11)

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 * 63 * 78 * 14 = 1788696.

What is the greatest product of four adjacent numbers in the
same direction (up, down, left, right, or diagonally) in the
20 x 20 grid?
"""

from numpy import product as prod

grid_s = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08\n49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00\n81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65\n52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91\n22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80\n24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50\n32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70\n67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21\n24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72\n21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95\n78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92\n16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57\n86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58\n19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40\n04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66\n88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69\n04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36\n20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16\n20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54\n01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"

def turn_to_array(grid: str) -> list[str]:
    grid = grid.split("\n")
    for i in range(len(grid)):
        grid[i] = grid[i].split(" ")
        grid[i] = [int(j) for j in grid[i]]
    return grid
    

def max_prod_array(a: list[int]) -> int:
    r = 3
    max_a = 0
    while r < len(a):
        if a[r] == 0:
            r += 4
        else:
            max_a = max(max_a,
                        prod(a[r - 3: r + 1]))
            r += 1
    return max_a


def euler011(g: list[list[int]]) -> int:
    # Searching line by line
    max_line = 0
    for line in g:
        max_line = max(max_line, max_prod_array(line))
    print("max_line =", max_line)

    # Searching column by column
    max_column = 0
    for c in range(len(g)):
        column = [line[c] for line in g]
        max_column = max(max_column, max_prod_array(column))
    print("max_column =", max_column)

    # Searching diagonal by diagonal
    max_diagonal = 0
    diagonals = list()
    for i in range(3, len(g[0])):
        c = i
        l = 0
        diagonal = list()
        while c >= 0:
            diagonal.append(g[l][c])
            l += 1
            c -= 1
        diagonals.append(diagonal)

    for i in range(1, len(g[19]) - 3):
        c = i
        l = 19
        diagonal = list()
        while c < len(g[19]):
            diagonal.append(g[l][c])
            l -= 1
            c += 1
        diagonal.reverse()
        diagonals.append(diagonal)
    
    for i in range(len(g[0]) - 3):
        c = i
        l = 0
        diagonal = list()
        while c <= 19:
            diagonal.append(g[l][c])
            l += 1
            c += 1
        diagonals.append(diagonal)
    

    for i in range(1, len(g[19]) - 3):
        c = 0
        l = i
        diagonal = list()
        while l <= 19:
            diagonal.append(g[l][c])
            l += 1
            c += 1
        diagonals.append(diagonal)

    for diag in diagonals:
        max_diagonal = max(max_diagonal,
                           max_prod_array(diag))
    print("max_diagonal =", max_diagonal)
    
    return max(max_line, max_column, max_diagonal)
    
    

grid = turn_to_array(grid_s)
print(euler011(grid))


sum = 0
with open("Advent-2023/day3.txt") as f:
    grid = f.read().splitlines()

    num_set = set()
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch.isdigit() or ch == ".":
                continue
            for curr_row in [r - 1, r, r + 1]:
                for curr_col in [c - 1, c, c + 1]:
                    if curr_row < 0 or curr_row >= len(grid) or curr_col < 0 or curr_col >= len(grid[curr_row]) or not grid[curr_row][curr_col].isdigit():
                        continue
                    while curr_col > 0 and grid[curr_row][curr_col - 1].isdigit():
                        curr_col -= 1
                    num_set.add((curr_row, curr_col))
    
    for row, col in num_set:
        s = ""
        while col < len(grid[row]) and grid[row][col].isdigit():
            s += grid[row][col]
            col += 1
        sum += int(s)
print(sum)

sum = 0
with open("Advent-2023/day3.txt") as f:
    grid = f.read().splitlines()
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch.isdigit() or ch == ".":
                continue
            num_set = set()
            for curr_row in [r - 1, r, r + 1]:
                for curr_col in [c - 1, c, c + 1]:
                    if curr_row < 0 or curr_row >= len(grid) or curr_col < 0 or curr_col >= len(grid[curr_row]) or not grid[curr_row][curr_col].isdigit():
                        continue
                    while curr_col > 0 and grid[curr_row][curr_col - 1].isdigit():
                        curr_col -= 1
                    num_set.add((curr_row, curr_col))
            if len(num_set) == 2:
                num = 1
                for row, col in num_set:
                    s = ""
                    while col < len(grid[row]) and grid[row][col].isdigit():
                        s += grid[row][col]
                        col += 1
                    num *= int(s)
                sum += num
print(sum)

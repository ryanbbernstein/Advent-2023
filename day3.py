
sum = 0
with open("Advent-2023/day3.txt") as f:
    grid = f.read().splitlines()

    num_set = set()
    for row_index, row in enumerate(grid):
        for col_index, char in enumerate(row):
            if char.isdigit() or char == ".":
                continue
            for curr_row in [row_index - 1, row_index, row_index + 1]:
                for curr_col in [col_index - 1, col_index, col_index + 1]:
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
    for row_index, row in enumerate(grid):
        for col_index, char in enumerate(row):
            if char.isdigit() or char == ".":
                continue
            num_set = set()
            for curr_row in [row_index - 1, row_index, row_index + 1]:
                for curr_col in [col_index - 1, col_index, col_index + 1]:
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

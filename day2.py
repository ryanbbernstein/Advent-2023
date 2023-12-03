
import math


bag_contents = {
    "red": 12,
    "green": 13,
    "blue": 14
}

sum = 0
with open("2023/day2.txt") as f:
    for l in f.readlines():
        s = l.strip().removeprefix("Game")
        id, game = s.split(":")
        reveals = game.strip().split(";")
        valid = True
        for reveal in reveals:
            cubes = reveal.split(",")
            for cube in cubes:
                num, color = cube.strip().split(" ")
                if color not in bag_contents or int(num) > bag_contents[color]:
                    valid = False
        if valid:
            sum += int(id)
print(sum)


sum = 0
with open("2023/day2.txt") as f:
    for l in f.readlines():
        s = l.strip().removeprefix("Game")
        id, game = s.split(":")
        reveals = game.strip().split(";")
        
        min_blue = 0
        min_green = 0
        min_red = 0

        for reveal in reveals:
            cubes = reveal.split(",")
            for cube in cubes:
                num, color = cube.strip().split(" ")
                if color == "blue":
                    min_blue = max(min_blue, int(num))
                elif color == "green":
                    min_green = max(min_green, int(num))
                elif color == "red":
                    min_red = max(min_red, int(num))
        sum += (min_blue * min_green * min_red)
print(sum)
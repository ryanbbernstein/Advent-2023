
sum = 0
with open("Advent-2023/day1.txt") as f:
    for l in f.readlines():
        s = l.strip()
        first = ""
        last = ""
        for character in s:
            if character.isnumeric():
                if first == "":
                    first = character
                    last = character
                else:
                    last = character
        num = f"{first}{last}"
        sum += int(num) if num.isnumeric() else 0
print(sum)

mapping = {
"one": "1", 
"two": "2", 
"three": "3", 
"four": "4", 
"five": "5", 
"six": "6", 
"seven": "7", 
"eight": "8", 
"nine": "9"
}

sum = 0
with open("Advent-2023/day1.txt") as f:
    for l in f.readlines():
        s = l.strip()
        for k,v in mapping.items():
            if k in s:
                while k in s:
                    index = s.find(k)
                    s = s[:index + 1] + v + s[index + 1:]
        first = ""
        last = ""
        for character in s:
            if character.isnumeric():
                if first == "":
                    first = character
                    last = character
                else:
                    last = character
        sum += int(f"{first}{last}")
print(sum)
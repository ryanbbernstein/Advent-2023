
sum = 0
with open("Advent-2023/day4.txt") as f:
    for card in f.readlines():
        card.strip()
        card = card.split(":")[1].strip()
        winning, numbers = card.split(" | ")
        winning = winning.split()
        points = 0
        for num in numbers.split():
            if num in winning:
                if points == 0:
                    points = 1
                else:
                    points *= 2
        sum += points
print(sum)

extra_cards = []
with open("Advent-2023/day4.txt") as f:
    num_cards = 0
    for card in f.readlines():
        num_cards += 1
        card.strip()
        card_num, card = card.split(":")
        card_num = card_num.split()[1]
        winning, numbers = card.split(" | ")
        winning = winning.strip().split()
        count = 0
        for num in numbers.split():
            if num in winning:
                count += 1
        extras = extra_cards.count(int(card_num))
        while count > 0:
            for _ in range(extras + 1):
                extra_cards.append(int(card_num) + count)
            count -= 1

print(num_cards + len(extra_cards))
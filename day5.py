from math import inf
import itertools

def parse_ranges(line_index, lines, ranges):
    line_index += 1
    while line_index < len(lines) and lines[line_index] != "":
        dest_start, source_start, length = lines[line_index].split()
        ranges.append((int(dest_start), int(source_start), int(length)))
        line_index += 1
    return line_index

with open("Advent-2023/day5.txt") as f:
    seeds = [int(i) for i in f.readline().removeprefix("seeds: ").split()]
    f.readline()
    lines = f.read().splitlines()
    line_index = 0
    
    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []
    
    while line_index < len(lines):
        if lines[line_index].startswith("seed-to-soil map:"):
            parse_ranges(line_index, lines, seed_to_soil)
        elif lines[line_index].startswith("soil-to-fertilizer map:"):
            parse_ranges(line_index, lines, soil_to_fertilizer)
        elif lines[line_index].startswith("fertilizer-to-water map:"):
            parse_ranges(line_index, lines, fertilizer_to_water)
        elif lines[line_index].startswith("water-to-light map:"):
            parse_ranges(line_index, lines, water_to_light)
        elif lines[line_index].startswith("light-to-temperature map:"):
            parse_ranges(line_index, lines, light_to_temperature)
        elif lines[line_index].startswith("temperature-to-humidity map:"):
            parse_ranges(line_index, lines, temperature_to_humidity)
        elif lines[line_index].startswith("humidity-to-location map:"):
            parse_ranges(line_index, lines, humidity_to_location)
        line_index += 1
    
    def get_from_range(range_table, value):
        for dest_start, source_start, length in range_table:
            if source_start <= value and value < source_start + length:
                return dest_start + (value - source_start)
        return value

    min_loc = inf
    for seed in seeds:
        soil = get_from_range(seed_to_soil, seed)
        fert = get_from_range(soil_to_fertilizer, soil)
        water = get_from_range(fertilizer_to_water, fert)
        light = get_from_range(water_to_light, water)
        temp = get_from_range(light_to_temperature, light)
        hum = get_from_range(temperature_to_humidity, temp)
        loc = get_from_range(humidity_to_location, hum)
        min_loc = min(min_loc, loc)
    print(min_loc)


with open("Advent-2023/day5.txt") as f:
    seeds = [int(i) for i in f.readline().removeprefix("seeds: ").split()]
    seeds = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]

    f.readline()
    lines = f.read().splitlines()
    line_index = 0
    
    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []
    
    while line_index < len(lines):
        if lines[line_index].startswith("seed-to-soil map:"):
            parse_ranges(line_index, lines, seed_to_soil)
        elif lines[line_index].startswith("soil-to-fertilizer map:"):
            parse_ranges(line_index, lines, soil_to_fertilizer)
        elif lines[line_index].startswith("fertilizer-to-water map:"):
            parse_ranges(line_index, lines, fertilizer_to_water)
        elif lines[line_index].startswith("water-to-light map:"):
            parse_ranges(line_index, lines, water_to_light)
        elif lines[line_index].startswith("light-to-temperature map:"):
            parse_ranges(line_index, lines, light_to_temperature)
        elif lines[line_index].startswith("temperature-to-humidity map:"):
            parse_ranges(line_index, lines, temperature_to_humidity)
        elif lines[line_index].startswith("humidity-to-location map:"):
            parse_ranges(line_index, lines, humidity_to_location)
        line_index += 1
    
    def get_from_range(range_table, value):
        for dest_start, source_start, length in range_table:
            if dest_start <= value and value < dest_start + length:
                return source_start + (value - dest_start)
        return value

    for i in itertools.count():
        hum = get_from_range(humidity_to_location, i)
        temp = get_from_range(temperature_to_humidity, hum)
        light = get_from_range(light_to_temperature, temp)
        water = get_from_range(water_to_light, light)
        fert = get_from_range(fertilizer_to_water, water)
        soil = get_from_range(soil_to_fertilizer, fert)
        seed = get_from_range(seed_to_soil, soil)

        for start, num in seeds:
            if start <= seed and seed < start + num:
                print(i)
                exit()

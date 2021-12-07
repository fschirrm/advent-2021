import utils.utils as utils

crab_list = utils.read_comma_list("files/task7.txt")
crab_dict = {}
for elem in crab_list:
    if elem in crab_dict:
        crab_dict[elem] += 1
    else:
        crab_dict[elem] = 1
min_fuel = -1
h_pos = -1
for i in range(min(crab_list), max(crab_list) + 1):
    curr_fuel = 0
    for key in crab_dict:
        fuel_pos = abs(key - i) * crab_dict[key]
        curr_fuel += fuel_pos
    if (min_fuel == -1) or (curr_fuel < min_fuel):
        min_fuel = curr_fuel
        h_pos = i
print(f"Position={h_pos} und Minimum Fuel={min_fuel}")

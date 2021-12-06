import utils.utils as utils

steps = 80
fish_list = utils.read_comma_list("files/task6.txt")
for i in range(steps):
    fish_list = [elem - 1 for elem in fish_list]
    for j in range(len(fish_list)):
        if fish_list[j] < 0:
            fish_list[j] = 6
            fish_list.append(8)
print(f"Result={len(fish_list)}")

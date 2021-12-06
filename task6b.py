import utils.utils as utils

steps = 256
fish_list = utils.read_comma_list("files/task6.txt")
count_list = [0 for x in range(0, 9)]
for i in range(0, 9):
    count_list[i] = fish_list.count(i)
for i in range(steps):
    new_list = [0 for x in range(0, 9)]
    for j in range(8, 0, -1):
        new_list[j - 1] = count_list[j]
    new_list[6] += count_list[0]
    new_list[8] = count_list[0]
    count_list = new_list.copy()
print(sum(count_list))

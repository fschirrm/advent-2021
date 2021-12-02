import utils.utils as utils

c=utils.read_file("files/task2.txt")
for line in c:
    print(line[0], ' ', line[1])
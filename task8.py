import utils.utils as utils

c = utils.read_file("files/task8.txt")
# print(c)
num_digits = 0
for elem in c:
    delimiter = False
    for i in range(len(elem)):
        if elem[i] == "|":
            delimiter = True
        else:
            if delimiter and (
                (len(elem[i]) == 2)
                or (len(elem[i]) == 3)
                or (len(elem[i]) == 4)
                or (len(elem[i]) == 7)
            ):
                num_digits += 1
print(f"Number of esay digits = {num_digits}")

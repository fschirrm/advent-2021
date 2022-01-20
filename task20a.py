import utils.utils as utils


def new_field(curr_list, infinite_char):
    new_list = []
    new_list.append(infinite_char * (len(curr_list) + 2))
    for elem in curr_list:
        new_list.append(infinite_char + elem + infinite_char)
    new_list.append(infinite_char * (len(curr_list) + 2))
    return new_list


algo_str, pic_list = utils.read_pic_algo("files/task20_test.txt")
new_list = new_field(pic_list, ".")
print(pic_list)
print(new_list)
infinite_char = "."
for i in range(new_list):
    for j in range(new_list[i]):
        pos = 0
        nr_algo = 0
        for m in range(-1, 2):
            for n in range(-1, 2):
                l_pos = i + m
                s_pos = i + n
                if (
                    (l_pos < 0)
                    or (s_pos < 0)
                    or (l_pos >= len(new_list))
                    or (s_pos >= len(new_list[i]))
                ):
                    if infinite_char == "#":
                        nr_algo += 2 ** pos

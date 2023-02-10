import utils.utils as utils

def new_field(curr_list, infinite_char):
    new_list = []
    new_list.append(infinite_char * (len(curr_list) + 2))
    for elem in curr_list:
        new_list.append(infinite_char + elem + infinite_char)
    new_list.append(infinite_char * (len(curr_list) + 2))
    return new_list

algo_str, pic_list = utils.read_pic_algo("files/task20.txt")
infinite_char = '.'
for rounds in range(50):
    new_list = new_field(pic_list, infinite_char)
    round_list = []
    for i in range(len(new_list)):
        round_row = ''
        for j in range(len(new_list[i])):
            pos = 8
            nr_algo = 0
            for m in range(-1, 2):
                for n in range(-1, 2):
                    l_pos = i + m
                    s_pos = j + n
                    if (
                        (l_pos < 0)
                        or (s_pos < 0)
                        or (l_pos >= len(new_list))
                        or (s_pos >= len(new_list[i]))
                    ):
                        if infinite_char == "#": nr_algo += 2 ** pos
                    else:
                        if new_list[l_pos][s_pos] == "#": nr_algo += 2 ** pos
                    pos -= 1
            round_row += algo_str[nr_algo]
        round_list.append(round_row)
    pic_list = round_list
    if infinite_char == '.': infinite_char = algo_str[0]
    else: infinite_char = algo_str[511]
    # for elem in pic_list:
    #     print(elem)
    # print()
num_pics = 0
for elem in pic_list:
    num_pics += elem.count('#')
print(f"Number of pics = {num_pics}")
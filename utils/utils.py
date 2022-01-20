def read_file(f):
    with open(f) as f:
        content = [line.strip().split(" ") for line in f.readlines()]
    return content


def read_num_list(f):
    num_field = []
    with open(f) as f:
        line = f.readline()
        while line:
            char_list = list(line.strip())
            num_field.append([int(c1) for c1 in char_list])
            line = f.readline()
    return num_field


def read_orig(f):
    orig_list = [[False for i in range(1500)] for j in range(1500)]
    with open(f) as f:
        line = f.readline()
        while line != "\n":
            coord = line.strip().split(",")
            orig_list[int(coord[1])][int(coord[0])] = True
            line = f.readline()
        line = f.readline()
        instr_list = []
        while line:
            inp = line.strip().split()
            instr = inp[2].split("=")
            instr_list.append((instr[0], int(instr[1])))
            line = f.readline()
    return orig_list, instr_list


def read_poly(f):
    rule_list = []
    with open(f) as f:
        line = f.readline()
        poly_list = list(line.strip())
        f.readline()
        line = f.readline()
        while line:
            inp = line.strip().split()
            rule_list.append([[inp[0][0], inp[0][1]], inp[2]])
            line = f.readline()
    return poly_list, rule_list


def read_beacon(f):
    beacon_list = []
    with open(f) as f:
        line = f.readline()
        while line:
            if line[0:3] == "---":
                new_scan = []
                beacon_list.append(new_scan)
            else:
                if line != "\n":
                    entry = line.strip().split(",")
                    entry_int = []
                    for elem in entry:
                        entry_int.append(int(elem))
                    new_scan.append([entry_int])
            line = f.readline()
    return beacon_list


def read_bingo(f):
    with open(f) as f:
        content = f.readlines()
    num_list = [int(str_num) for str_num in content[0].strip().split(",")]
    bingo_list = []
    for i in range(1, len(content)):
        line = content[i].strip()
        if len(line) == 0:
            curr_bingo = []
            bingo_list.append(curr_bingo)
        else:
            curr_bingo.append([int(str_num) for str_num in line.split()])
    if bingo_list[-1] == []:
        bingo_list.remove([])
    return num_list, bingo_list


def read_comma_list(f):
    with open(f) as f:
        content = f.readline()
    return [int(x) for x in content.split(",")]


def read_pic_algo(f):
    with open(f) as f:
        algo_str = f.readline().strip()
        f.readline()
        line = f.readline()
        pic_list = []
        while line:
            inp = line.strip()
            pic_list.append(inp)
            line = f.readline()
    return algo_str, pic_list

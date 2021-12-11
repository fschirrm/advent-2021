def read_file(f):
    with open(f) as f: 
        content = [line.strip().split(" ") for line in f.readlines()]
    return content

def read_num_list(f):
    num_field=[]
    with open(f) as f:
        line = f.readline()
        while line:
            num_field.append(list(line.strip()))
            line = f.readline()
    return num_field

def read_bingo(f):
    with open(f) as f:
        content=f.readlines()
    num_list = [int(str_num) for str_num in content[0].strip().split(",")]
    bingo_list=[]
    for i in range(1,len(content)):
        line= content[i].strip()
        if len(line) == 0:
            curr_bingo = []
            bingo_list.append(curr_bingo)
        else:
            curr_bingo.append([int(str_num) for str_num in line.split()])
    if bingo_list[-1] == []: bingo_list.remove([])
    return num_list, bingo_list

def read_comma_list(f):
    with open(f) as f: content=f.readline()
    return [int(x) for x in content.split(',')]
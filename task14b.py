import utils.utils as utils

def add_poly(elem, frequ_dict, l_dict):
    if elem[0] in frequ_dict: frequ_dict[elem[0]] += 1
    else: frequ_dict[elem[0]] = 1
    if elem in l_dict: l_dict[elem] += 1
    return frequ_dict, l_dict

poly_list, raw_list = utils.read_poly("files/task14.txt")

rule_dict ={}
loop_dict = {}
for elem in raw_list:
    key = "".join(elem[0])
    rule_dict[key] = [elem[1]]
    loop_dict[key] = 0
for k in rule_dict:
    new_elem1 = k[0] + rule_dict[k][0]
    new_elem2 = rule_dict[k][0] + k[1]
    result_list = []
    if new_elem1 in rule_dict: result_list.append(new_elem1)
    if new_elem2 in rule_dict: result_list.append(new_elem2)
    rule_dict[k].append(result_list)

frequ_dict = {}
loop_dict_work = loop_dict.copy()
for i in range(len(poly_list)-1):
    frequ_dict, loop_dict = add_poly(poly_list[i] + poly_list[i+1], frequ_dict, loop_dict)
if poly_list[-1] in frequ_dict: frequ_dict[poly_list[-1]] += 1
else: frequ_dict[poly_list[-1]] = 1

for i in range(40):
    for k in loop_dict:
        if loop_dict[k] > 0: 
            if rule_dict[k][0] in frequ_dict: frequ_dict[rule_dict[k][0]] += loop_dict[k]
            else: frequ_dict[rule_dict[k][0]] = loop_dict[k]
            for elem in rule_dict[k][1]:
                loop_dict_work[elem] += loop_dict[k]
    loop_dict = loop_dict_work.copy()
    for k in loop_dict_work: loop_dict_work[k] = 0
    max = -1; min = -1
    max_key = ''; min_key = ''
    for k in frequ_dict:
        if frequ_dict[k] > max:
            max = frequ_dict[k]
            max_key = k
        if (frequ_dict[k] < min) or (min == -1):
            min = frequ_dict[k]
            min_key = k
print (f"Min: {min_key}={min}")
print (f"Max: {max_key}={max}")
print (f"Result: {max - min}")
    
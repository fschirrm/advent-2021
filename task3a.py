import utils.utils as utils

c = utils.read_file("files/task3.txt")
l1 = list(c[0][0])
result_list = []
for c1 in l1:
    result_list.append([])
for line in c:
    new_list = list(line[0])
    for i in range(0, len(new_list)):
        result_list[i].append(new_list[i])
gama_str = ""
for l2 in result_list:
    if l2.count("1") > len(l2) / 2:
        gama_str = gama_str + "1"
    else:
        gama_str = gama_str + "0"
gama = int(gama_str, 2)
eps_str = ""
for i in range(0, len(gama_str)):
    if gama_str[i] == "1":
        eps_str = eps_str + "0"
    else:
        eps_str = eps_str + "1"
eps = int(eps_str, 2)
print(f"Result={gama*eps}")

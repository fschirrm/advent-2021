import utils.utils as utils

c = utils.read_file("files/task3.txt")
oxy_list = []
for line in c:
    l1 = list(line[0])
    oxy_list.append(l1)
co2_list = oxy_list.copy()
for i in range(0, len(oxy_list[0])):
    count1 = 0
    for l2 in oxy_list:
        if l2[i] == "1":
            count1 += 1
    if count1 >= len(oxy_list) / 2:
        most_common = "1"
    else:
        most_common = "0"
    del_nr = 0
    for j in range(0, len(oxy_list)):
        if oxy_list[j - del_nr][i] != most_common:
            oxy_list.pop(j - del_nr)
            del_nr += 1
    if len(oxy_list) <= 1:
        break
print(oxy_list)
for i in range(0, len(co2_list[0])):
    count0 = 0
    for l2 in co2_list:
        if l2[i] == "0":
            count0 += 1
    if count0 <= len(co2_list) / 2:
        less_common = "0"
    else:
        less_common = "1"
    del_nr = 0
    for j in range(0, len(co2_list)):
        if co2_list[j - del_nr][i] != less_common:
            co2_list.pop(j - del_nr)
            del_nr += 1
    if len(co2_list) <= 1:
        break
print(co2_list)
oxy_str = "".join(oxy_list[0])
oxy_nr = int(oxy_str, 2)
co2_str = "".join(co2_list[0])
co2_nr = int(co2_str, 2)
print(f"Result={oxy_nr*co2_nr}")

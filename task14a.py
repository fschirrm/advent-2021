import utils.utils as utils
from collections import Counter

poly_list, rule_list = utils.read_poly("files/task14_test.txt")
# print(poly_list); print(); print(rule_list)
for i in range(10):
    new_poly_list = [poly_list[0]]
    for j in range(len(poly_list)-1):
        for elem in rule_list:
            if (poly_list[j] == elem[0][0]) and (poly_list[j+1] == elem[0][1]):
                new_poly_list.append(elem[1])
                break
        new_poly_list.append(poly_list[j+1])
    poly_list = new_poly_list

frequ = Counter(poly_list)
frequ_list = frequ.most_common()
print (frequ_list[0][1] - frequ_list[-1][1])
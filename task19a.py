import utils.utils as utils

beacon_list = utils.read_beacon("files/task19_test.txt")
for scanner in beacon_list:
    for beacon in scanner:
        rel_list = []
        for b1 in scanner:
            x =  b1[0][0] - beacon[0][0]
            y =  b1[0][1] - beacon[0][1]
            z =  b1[0][2] - beacon[0][2]
            rel_list.append([x,y,z])
        beacon.append(rel_list)

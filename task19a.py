import utils.utils as utils

def find_beacon (s1, s2):
    permut_list = [[0,1,2],[1,0,2],[2,1,0],[0,2,1],[2,0,1],[1,2,0]]
    point_list=[]
    arrangement = []
    found = False
    for permut in permut_list:
        for m in range(len(s1)):
            if s1[m][0]!=0 or s1[m][1]!=0 or s1[m][2]!=0:
                for n in range(len(s2)):
                    if abs(s1[m][0]) == abs(s2[n][0]) and abs(s1[m][1]) == abs(s2[n][1]) and \
                        abs(s1[m][2]) == abs(s2[n][2]):
                        point_list.append(m)
                        orient = []
                        for k in range(3):
                            if s1[m][k] == s2[n][k]: orient.append(1)
                            else: orient.append(-1)
        if len(point_list) >= 11:
            arrangement = permut
            found = True
            break
        else: point_list = []
    return found, point_list, arrangement, orient

def compare_scanner(scanner1, scanner2):
    found = False
    for i in range(len(scanner1)):
        point_list = []
        for j in range(len(scanner2)):
            found, point_list, arrangement, orient = find_beacon (scanner1[i][1], scanner2[j][1])
            point_list.append(i)
            if found: break
        if found: 
            scanner_pos = []
            for k in range(3):
                scanner_pos.append(scanner1[i][0][k] - scanner2[j][0][arrangement[k]]*orient[k])
            break
    return found, point_list, arrangement, orient, scanner_pos

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
#print(beacon_list[0][0])
found, point_list, arrangement, orient, scanner_pos = compare_scanner(beacon_list[0], beacon_list[1])
print(found); 
print(arrangement)
print(orient)
print(scanner_pos)
print()
for elem in point_list: print(beacon_list[0][elem][0]); 
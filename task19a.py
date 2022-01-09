import utils.utils as utils

def find_beacon (s1, s2):
    permut_list = [[0,1,2],[1,0,2],[2,1,0],[0,2,1],[2,0,1],[1,2,0]]
    point_list=[]
    arrangement = []
    orient = []
    found = False
    for permut in permut_list:
        for m in range(len(s1)):
            if s1[m][0]!=0 or s1[m][1]!=0 or s1[m][2]!=0:
                for n in range(len(s2)):
                    if abs(s1[m][0]) == abs(s2[n][permut[0]]) and abs(s1[m][1]) == abs(s2[n][permut[1]]) and \
                        abs(s1[m][2]) == abs(s2[n][permut[2]]):
                        point_list.append(m)
                        orient = []
                        for k in range(3):
                            if s1[m][k] == s2[n][permut[k]]: orient.append(1)
                            else: orient.append(-1)
        if len(point_list) >= 11:
            arrangement = permut
            found = True
            break
        else: point_list = []
    return found, point_list, arrangement, orient

def compare_scanner(scanner1, scanner2):
    found = False
    arrangement = []; orient = []; scanner_pos = []
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

def insert_points(s2, result_list, rel_pos, point_list, arrangement, orient):
    for m in range(len(s2)):
        point = []
        for k in range(3):
            point.append(rel_pos[k] + s2[m][0][arrangement[k]]*orient[k]) 
        point_found=False
        for elem in result_list:
            if (elem[0] == point[0]) and (elem[1] == point[1]) and (elem[2] == point[2]):
                point_found = True
                break
        if not point_found: result_list.append(point)
    return result_list

beacon_list = utils.read_beacon("files/task19.txt")
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
prep_list = [[0,[0,0,0],[0,1,2],[1,1,1]]]
rem_list = [i for i in range(1,len(beacon_list))]
result_list = []
for elem in beacon_list[0]: result_list.append(elem[0]) 
while (len(prep_list) > 0) and (len(rem_list) > 0):
    curr_elem = prep_list.pop(0)
    s1 = beacon_list[curr_elem[0]]
    new_rem_list = rem_list.copy()
    for elem in rem_list:
        s2 = beacon_list[elem]
        found, point_list, arrangement, orient, scanner_pos = compare_scanner(s1, s2)
        if found:
            print (f"Found in pair {curr_elem[0]} and {elem}" )
            rel_pos = []
            for k in range(3):
                pos_elem = curr_elem[1][k] + scanner_pos[curr_elem[2][k]] * curr_elem[3][k]
                rel_pos.append(pos_elem)
            s0_arrangement = [arrangement[curr_elem[2][0]],arrangement[curr_elem[2][1]], arrangement[curr_elem[2][2]]]
            s0_orient= [curr_elem[3][0]*orient[curr_elem[2][0]], curr_elem[3][1]*orient[curr_elem[2][1]], curr_elem[3][2]*orient[curr_elem[2][2]]]
            prep_list.append([elem,rel_pos, s0_arrangement, s0_orient])
            new_rem_list.remove(elem)
            result_list = insert_points(s2, result_list, rel_pos, point_list, s0_arrangement, s0_orient)
    rem_list = new_rem_list
print()
print(f"Number Beacons: {len(result_list)}"); 
#new_list=sorted(result_list,key=lambda p: p[0])

#for elem in new_list: print(elem); 
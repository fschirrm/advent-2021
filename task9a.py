import utils.utils as utils

c = utils.read_file("files/task9.txt")
heightmap = []
for elem in c:
    new_line = []
    for i in range(len(elem[0])):
        new_line.append(int(elem[0][i]))
    heightmap.append(new_line)
sum_risks = 0
low_points = []
for i in range(len(heightmap)):
    for j in range(len(heightmap[0])):
        if (i == 0) or (heightmap[i - 1][j] > heightmap[i][j]):
            if (j == 0) or (heightmap[i][j - 1] > heightmap[i][j]):
                if (i == len(heightmap) - 1) or (heightmap[i + 1][j] > heightmap[i][j]):
                    if (j == len(heightmap[i]) - 1) or (heightmap[i][j + 1] > heightmap[i][j]):
                        sum_risks += heightmap[i][j] + 1
                        low_points.append(heightmap[i][j])
print(f"Sum of Risks = {sum_risks}")
#print(low_points)

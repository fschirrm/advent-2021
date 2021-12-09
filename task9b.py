import utils.utils as utils


def count_basin(x, y, visit_map):
    basin = 1
    visit_map[x][y] = True
    if (
        (x > 0)
        and not visit_map[x - 1][y]
        and (heightmap[x - 1][y] > heightmap[x][y])
        and (heightmap[x - 1][y] < 9)
    ):
        basin += count_basin(x - 1, y, visit_map)
    if (
        (x < len(heightmap) - 1)
        and not visit_map[x + 1][y]
        and (heightmap[x + 1][y] > heightmap[x][y])
        and (heightmap[x + 1][y] < 9)
    ):
        basin += count_basin(x + 1, y, visit_map)
    if (
        (y > 0)
        and not visit_map[x][y - 1]
        and (heightmap[x][y - 1] > heightmap[x][y])
        and (heightmap[x][y - 1] < 9)
    ):
        basin += count_basin(x, y - 1, visit_map)
    if (
        (y < len(heightmap[0]) - 1)
        and not visit_map[x][y + 1]
        and (heightmap[x][y + 1] > heightmap[x][y])
        and (heightmap[x][y + 1] < 9)
    ):
        basin += count_basin(x, y + 1, visit_map)
    return basin


def init_visit_map(base_map):
    visit_map = []
    for n in range(len(base_map)):
        visit_map.append([False for elem in base_map[n]])
    return visit_map


c = utils.read_file("files/task9.txt")
heightmap = []
for elem in c:
    new_line = []
    for i in range(len(elem[0])):
        new_line.append(int(elem[0][i]))
    heightmap.append(new_line)
sum_risks = 0
low_points = []
basin_list = []
for i in range(len(heightmap)):
    for j in range(len(heightmap[0])):
        if (i == 0) or (heightmap[i - 1][j] > heightmap[i][j]):
            if (j == 0) or (heightmap[i][j - 1] > heightmap[i][j]):
                if (i == len(heightmap) - 1) or (heightmap[i + 1][j] > heightmap[i][j]):
                    if (j == len(heightmap[i]) - 1) or (heightmap[i][j + 1] > heightmap[i][j]):
                        sum_risks += heightmap[i][j] + 1
                        low_points.append(heightmap[i][j])
                        basin_list.append(count_basin(i, j, init_visit_map(heightmap)))
basin_list.sort(reverse=True)
sum_risks = basin_list[0] * basin_list[1] * basin_list[2]
print(f"Sum of Risks = {sum_risks}")
# print(low_points)
# print(basin_list)

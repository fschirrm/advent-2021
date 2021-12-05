import utils.utils as utils

dimension=1000
c = utils.read_file("files/task5.txt")
grid=[[0 for x in range(dimension)] for y in range(dimension)]
for i in range (0,len(c)):
    start_coord = [int(x) for x in c[i][0].split(',')]
    end_coord = [int(x) for x in c[i][2].split(',')]
    num_points=0
    if start_coord[0] < end_coord[0]: 
        x_add=1; num_points=end_coord[0]-start_coord[0]+1
    else:  
        if start_coord[0] > end_coord[0]: 
            x_add=-1; num_points=start_coord[0]-end_coord[0]+1
        else: x_add=0
    if start_coord[1] < end_coord[1]: 
        y_add=1; num_points=end_coord[1]-start_coord[1]+1
    else:  
        if start_coord[1] > end_coord[1]: 
            y_add=-1; num_points=start_coord[1]-end_coord[1]+1
        else: y_add=0
    curr_x=start_coord[0]; curr_y=start_coord[1]
    for j in range(0,num_points):
        grid[curr_x][curr_y]+=1
        curr_x+=x_add; curr_y+=y_add 
    #print(start_coord,'  ',end_coord,'  ',num_points )
    #print(grid)
count=0
for i in range(0,dimension):
    for j in range (0,dimension):
        if grid[i][j] > 1: count+=1
print (f"Number of overlapping points: {count}")
    
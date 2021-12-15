import utils.utils as utils

path_list = []
curr_short_risk = 0
inp_list = utils.read_num_list("files/task15.txt")
print(inp_list)

def search_path (x,y,risk,curr_path):
    global curr_short_risk
    global path_list
    if x!=0 or y!=0: risk += inp_list[x][y]
    if risk >= curr_short_risk  : return
    if (x==(len(inp_list)-1)) and (y==(len(inp_list[len(inp_list)-1])-1)):
        path_list=curr_path
        curr_short_risk=risk
        print(curr_short_risk)
        print(path_list)
    if x<len(inp_list)-1: search_path (x+1,y,risk,curr_path+[(x+1,y)])
    if y<len(inp_list[0])-1: search_path (x,y+1,risk,curr_path+[(x,y+1)])
    #if x>0 and x==path_list[-1][0]: search_path (x-1,y,risk,curr_path+[(x-1,y)])
    #if y>0 and y==path_list[-1][1]: search_path (x,y-1,risk,curr_path+[(x,y-1)])
    return
    
i=0; j=0
while (i<len(inp_list)-1) and (j<len(inp_list[0])-1):
    path_list.append((i,j))
    if i>0 or j> 0: curr_short_risk += inp_list[i][j]
    if (i<len(inp_list)-1):
        if (j<len(inp_list)-1):
            if inp_list[i+1][j]<=inp_list[i][j+1]: i+=1
            else: j+=1
        else: i+=1
    else: j+=1
print(curr_short_risk)
print(path_list)
search_path(0,0,0,[])
print()
print(curr_short_risk)
import utils.utils as utils

steps=100

def get_neighbours(a,b,max_a,max_b):
    n_full = [(a-1,b-1),(a-1,b),(a-1,b+1),(a,b-1),(a,b+1),(a+1,b-1),(a+1,b),(a+1,b+1)]
    neighbours = [(x,y) for (x,y) in n_full if (x>=0) and (y>=0) and (x<max_a) and y<max_b]
    return(neighbours)
    
inp_list = utils.read_num_list("files/task11.txt")
curr_list = inp_list
flash_count = 0
rounds = 0
while(True):
    rounds += 1
    flash_list = []
    #curr_list = step_list[i].copy()
    for elem in curr_list:
        flash_line = [False for e1 in elem]
        flash_list.append(flash_line) 
    for m in range(len(curr_list)):
        for n in range(len(curr_list[0])): curr_list[m][n]+=1
    round_count=0
    while True:       
        nothing_changed=True     
        for m in range(len(curr_list)):
            for n in range(len(curr_list[0])): 
                if not flash_list[m][n] and curr_list[m][n] > 9:
                    curr_list[m][n]=0
                    flash_list[m][n]=True
                    flash_count+=1; round_count += 1
                    nothing_changed=False
                    n_list = get_neighbours(m,n,len(curr_list),len(curr_list[0]))
                    for elem in n_list:
                        if not flash_list[elem[0]][elem[1]]:
                            curr_list[elem[0]][elem[1]]+=1
        if nothing_changed: break
    if (round_count >= 100) or (rounds > 10000): break
print(f"Rounds necessary: {rounds}")





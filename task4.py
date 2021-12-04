import utils.utils as utils

num_list, bingo_list = utils.read_bingo("files/task4.txt")

status_list =[]
for l in bingo_list:
    new_list=[]
    for elem in l:
        new_list1=[]
        for elem1 in l:
            new_list1.append(False)
        new_list.append(new_list1)
    status_list.append(new_list)
finish=False
end_num=0
winnig_board = []
winning_status_borad = []
for num in num_list:
    for i in range(0,len(bingo_list)):
        for j in range (0, len(bingo_list[i])):
            for k in range (0,len(bingo_list[i][j])):
                if bingo_list[i][j][k] == num:
                    status_list[i][j][k]=True
                    found = True
                    for elem in status_list[i][j]: 
                        if not elem: found=False; break
                    if not found:
                        found=True
                        for l in range (0, len(bingo_list[i])):
                            if not status_list[i][l][k]: found=False
                    if found: 
                        finish=True
                        end_num=num
                        winning_board = bingo_list[i]
                        winning_status_board = status_list[i]
                        break
            if finish: break
        if finish: break
    if finish: break   
unmarked_used=[]; unmarked_num=0
for i in range (0, len(winning_board)):
    for j in range (0,len(winning_board[i])):
        if not winning_status_board[i][j]:
            if not (winning_board[i][j] in unmarked_used):
                unmarked_num +=  winning_board[i][j]
                unmarked_used.append(winning_board[i][j])
print (f"Unset Value: {unmarked_num}")
print (f"Last Number: {end_num}")
print (f"Result: {unmarked_num*end_num}")
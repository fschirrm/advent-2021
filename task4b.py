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
end_num=0
last_board = []
last_status_board = []
finished=False
for num in num_list:
    if finished: break
    else:
        boards_found=0
        for i in range(0,len(bingo_list)):
            if finished: break
            else:
                board_removed=False
                for j in range (0, len(bingo_list[i-boards_found])):
                    for k in range (0,len(bingo_list[i-boards_found][j])):
                        if bingo_list[i-boards_found][j][k] == num:
                            status_list[i-boards_found][j][k]=True
                            found = True
                            for elem in status_list[i-boards_found][j]: 
                                if not elem: found=False; break
                            if found: 
                                end_num=num
                                last_board = bingo_list[i-boards_found]
                                last_status_board = status_list[i-boards_found]
                                bingo_list.pop(i-boards_found)
                                status_list.pop(i-boards_found)
                                board_removed=True
                                boards_found += 1
                                if len(bingo_list)==0: finished=True
                                break
                    if board_removed: break
unmarked_used=[]; unmarked_num=0
for i in range (0, len(last_board)):
    for j in range (0,len(last_board[i])):
        if not last_status_board[i][j]:
            if not (last_board[i][j] in unmarked_used):
                unmarked_num +=  last_board[i][j]
                unmarked_used.append(last_board[i][j])
print (f"Unset Value: {unmarked_num}")
print (f"Last Number: {end_num}")
print (f"Result: {unmarked_num*end_num}")
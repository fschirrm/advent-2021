start_pos_p1 = 7
start_pos_p2 = 9


def count_univ(player_list, die_const, act_player):
    result_list = [0, 0]
    sec_player = (act_player + 1) % 2
    for i in range(3, 10):
        player_list_new = []
        for elem in player_list:
            player_list_new.append(elem.copy())
        player_list_new[act_player][0] = ((player_list[act_player][0] - 1 + i) % 10) + 1
        player_list_new[act_player][1] += player_list_new[act_player][0]
        if player_list_new[act_player][1] < 21:
            r1_list = count_univ(player_list_new, die_const, sec_player)
            result_list[0] += die_const[i] * r1_list[0]
            result_list[1] += die_const[i] * r1_list[1]
        else:
            result_list[act_player] += die_const[i]
    return result_list


die_const = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            pos = i + j + k
            die_const[pos] += 1

player_list = [[start_pos_p1, 0], [start_pos_p2, 0]]
univ_list = count_univ(player_list, die_const, 0)
print(univ_list)
if univ_list[0] > univ_list[1]:
    print(f"Result={univ_list[0]}")
else:
    print(f"Result={univ_list[1]}")

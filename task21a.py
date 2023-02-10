start_pos_p1 = 7
start_pos_p2 = 9
die = 1
num_rolls = 0
act_player = 0
player_list = [[start_pos_p1, 0], [start_pos_p2, 0]]

while (player_list[0][1] < 1000) and (player_list[1][1] < 1000):
    for i in range(3):
        player_list[act_player][0] = ((player_list[act_player][0] - 1 + die) % 10) + 1
        die = (die % 100) + 1
        num_rolls += 1
    player_list[act_player][1] += player_list[act_player][0]
    if act_player == 0:
        act_player = 1
    else:
        act_player = 0
if player_list[0][1] < player_list[1][1]:
    result = player_list[0][1] * num_rolls
else:
    result = player_list[1][1] * num_rolls
print(f"Score Player 1 = {player_list[0][1]}")
print(f"Score Player 2 = {player_list[1][1]}")
print(f"Number rolls = {num_rolls}")
print(f"Result = {result}")

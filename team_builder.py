import csv


players_master_list = {}
player_current_list = {}

master_list_file = 'store/player_master_list.csv'
players_list_file = 'player_list.csv'

with open(master_list_file) as player_list:
    player_list_reader = csv.reader(player_list, delimiter=',')
    for player in player_list_reader:
        player_name = player[0].lower()
        player_overall_skill = int(player[1])
        players_master_list[player_name] = player_overall_skill


with open(players_list_file) as player_list:
    player_list_reader = csv.reader(player_list)
    for player in player_list_reader:
        player_name = player[0].lower()
        if player_name not in players_master_list:
            print(player_name + " not in the master list file!!!")
            exit(1)
        player_skill = players_master_list[player_name]
        player_current_list[player_name] = player_skill

sorted_players = sorted(player_current_list.items(), key=lambda kv: kv[1], reverse=True)


print(sorted_players)
print(sorted_players[0::2])
print(sorted_players[1::2])

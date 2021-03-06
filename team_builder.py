import csv
import random
import sys

MASTER_LIST_FILE = 'store/player_master_list.csv'
PLAYERS_LIST_FILE = 'player_list.csv'
NUM_OF_TEAMS = 2

TEAM_NAMES = [
    ("Ferocious", "Blazing", "Dashing", "Monumental", "Bombastic", "Galactic"),
    ("Pandas", "Rhinos", "Panthers", "Penguins", "Elephants")
]


# Read the master list file and create a dict
def build_master_list():
    master_list = {}
    with open(MASTER_LIST_FILE) as player_list:
        player_list_reader = csv.reader(player_list, delimiter=',')
        for player in player_list_reader:
            player_name = player[0].lower()
            player_overall_skill = int(player[1])
            master_list[player_name] = player_overall_skill
    return master_list


# Fetch the rating of players from master list and create a dict
def build_ranked_players(players_list_file, master_list):
    current_list = {}
    with open(players_list_file) as player_list:
        player_list_reader = csv.reader(player_list)
        for player in player_list_reader:
            player_name = player[0].lower()
            if player_name not in master_list:
                print(player_name + " not in the master list file!!!")
                exit(1)
            player_skill = master_list[player_name]
            current_list[player_name] = player_skill
    return current_list


# Pick random team names
def get_random_team_name():
    prefix = random.choice(TEAM_NAMES[0])
    suffix = random.choice(TEAM_NAMES[1])
    return prefix+" "+suffix


if __name__ == "__main__":
    if len(sys.argv) > 1:
        players_list_file = sys.argv[1]
    else:
        players_list_file = PLAYERS_LIST_FILE

    # Create a dict of players from the master list
    players_master_list = build_master_list()
    player_current_list = build_ranked_players(players_list_file, players_master_list)

    sorted_players = sorted(player_current_list.items(), key=lambda kv: kv[1], reverse=True)

    # Sort the players into teams
    for team_id in range(0, NUM_OF_TEAMS):
        team = sorted_players[0 + team_id::NUM_OF_TEAMS]
        team_names = map(lambda player: player[0], team)

        print("*" + get_random_team_name() + "*")
        print(*team_names, sep='\n')
        print('\n')
teams = {
    'Brazil': {
        'wins': 1, 
        'draws': 0, 
        'losses': 0, 
        'goals_for': 5, 
        'goals_against': 2
        }, 
    'Serbia': {
        'wins': 0, 
        'draws': 1, 
        'losses': 1, 
        'goals_for': 3, 
        'goals_against': 6
        }, 
    'Switzerland': {
        'wins': 0, 
        'draws': 1, 
        'losses': 1, 
        'goals_for': 2, 
        'goals_against': 4
        }, 
    'Costa_Rica': {
        'wins': 1, 
        'draws': 0, 
        'losses': 0, 
        'goals_for': 3, 
        'goals_against': 1
        }
    }

def make_list(dict):
    empty_list = []
    for items in dict:
        empty_list.append({"country" : items})
        
    return empty_list

x = make_list(teams)
print(x)
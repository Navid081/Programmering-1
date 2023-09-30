teams = {
    "Brazil": {
        "wins" : 0,
        "draws" : 0,
        "losses" : 0,
        "goals_for" : 0,
        "goals_against" : 0
    },
    "Serbia" : {
        "wins" : 0,
        "draws" : 0,
        "losses" : 0,
        "goals_for" : 0,
        "goals_against" : 0
    },
    "Switzerland" : {
        "wins" : 0,
        "draws" : 0,
        "losses" : 0,
        "goals_for" : 0,
        "goals_against" : 0
    },
    "Costa_Rica" : {
        "wins" : 0,
        "draws" : 0,
        "losses" : 0,
        "goals_for" : 0,
        "goals_against" : 0
    }
}

def add_game(home_team, home_score, away_team, away_score):
    if home_score > away_score:
        teams[home_team]["wins"] += 1
        teams[away_team]["losses"] += 1
    elif home_score == away_score:
        teams[home_team]["draws"] += 1
        teams[away_team]["draws"] += 1
    
    teams[home_team]["goals_for"] += home_score
    teams[away_team]["goals_for"] += away_score
    
    teams[home_team]["goals_against"] += away_score
    teams[away_team]["goals_against"] += home_score

    # Tre matcher har hållits hittils.
add_game("Brazil", 5, "Serbia", 2)
add_game("Costa_Rica", 3, "Switzerland", 1)
add_game("Serbia", 1, "Switzerland", 1)


ui_width = 40

brazil_wins = teams['Brazil']['wins']
brazil_draws = teams['Brazil']['draws']
brazil_losses = teams['Brazil']['losses']
brazil_goals_for = teams['Brazil']['goals_for']
brazil_goals_against = teams['Brazil']['goals_against']

# Använde variabler för brassarnas resultat, inga för de andra tre lagen.
print("-" * ui_width)
print("| Nation\t| W | D | L |GF |GA |")
print("-" * ui_width)
print(f"| Brazil\t| {brazil_wins} | {brazil_draws} | {brazil_losses} | {brazil_goals_for} | {brazil_goals_against} |")
print(f"| Serbia\t| {teams['Serbia']['wins']} | {teams['Serbia']['draws']} | {teams['Serbia']['losses']} | {teams['Serbia']['goals_for']} | {teams['Serbia']['goals_against']} |")
print(f"| Switzerland\t| {teams['Switzerland']['wins']} | {teams['Switzerland']['draws']} | {teams['Switzerland']['losses']} | {teams['Switzerland']['goals_for']} | {teams['Switzerland']['goals_against']} |")
print(f"| Costa_Rica\t| {teams['Costa_Rica']['wins']} | {teams['Costa_Rica']['draws']} | {teams['Costa_Rica']['losses']} | {teams['Costa_Rica']['goals_for']} | {teams['Costa_Rica']['goals_against']} |")


print(teams)
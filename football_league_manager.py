import tabulate

teams= []
while(1):
    temp = input("Enter team name: [Enter end to end.]")
    if temp == '':
        continue
    if temp.lower() == 'end':
        break
    temp_dict = globals()[temp] = {
        'team_name' : temp,
        'played':int(0),
        'points' :int(0),
        'won':int(0),
        'lose':int(0),
        'draw':int(0),
        'goaldiff':int(0)
    }
    teams.append(temp_dict)

# # Team list [name, played,Point, Won,lose, Draw, Goaldiff]
def vs_tuple(teama, home, away, teamb):
    for i in range(len(teams)):
        if teama == teams[i]['team_name']:
                for j in range(len(teams)):
                    if teamb == teams[j]['team_name']:
                        teams[i]['played']+=1
                        teams[j]['played']+=1

                        if home == away:
                            teams[i]['points']+=1
                            teams[j]['points']+=1
                            teams[i]['draw']+=1
                            teams[j]['draw']+=1
                        if home > away:
                            teams[i]['points']+=3
                            teams[i]['won']+=1
                            teams[j]['lose']+=1
                            teams[i]['goaldiff']+= (home -away)
                        if home < away:
                            teams[j]['points']+=3
                            teams[j]['won']+=1
                            teams[i]['lose']+=1
                            teams[j]['goaldiff']+= (away- home)  
                   

print("Enter the scores of team in order as:")

for i in range(len(teams)):
    for j in range(i+1,len(teams)):
        print(teams[i]['team_name'], " vs ", teams[j]['team_name'])
        home, away = int(input()), int(input())
        vs_tuple(teams[i]['team_name'], home,away, teams[j]['team_name'])
print("=====================")
print(teams) 
print("=========================")
for names in teams:
    for key,value in names.items():
        print(key, ' : ', value)
    print("================================")
def table_print(teams):
    header = teams[0].keys()
    rows = [x.values() for x in teams]
    print (tabulate.tabulate(rows,header))

table_print(teams)
print ("The list printed sorting by points and then goal difference whenever necessary: ")
sorted_teams = sorted(teams, key = lambda i: (i['points'], i['goaldiff']), reverse=True)
table_print(sorted_teams)
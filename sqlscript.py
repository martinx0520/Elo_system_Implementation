import psycopg2 as pg2

# Data Retrieval
conn = pg2.connect(database = 'Valorant10manStats', user = 'postgres', password = 'xwl020520')
cur = conn.cursor()

cur.execute('select player_name, elo from elo')
elo = cur.fetchall();

elo_dict = {}
for row in elo:
    elo_dict[row[0]] = row[1]

# vars and arrays
team1 = [0] * 5
team2 = [0] * 5
elo1 = [0] * 5
elo2 = [0] * 5
avg1 = 0
avg2 = 0
winner = ""
loser = ""
dif = 0
print("Input the members of Team 1:")
for i in range(5):
    team1[i] = input("Member: ")
    elo1[i] = elo_dict[team1[i]]
    avg1 += elo1[i]

avg1 = avg1 / 5 - 1000
print("Input the members of Team 2:")
for i in range(5):
    team2[i] = input("Member: ")
    elo2[i] = elo_dict[team2[i]]
    avg2 += elo2[i]

avg2 = avg2 / 5 - 1000
if avg1 > avg2:
    winner = "team1"
    loser = "team2"
    dif = avg1 - avg2
else:
    winner = "team2"
    loser = "team1"
    dif = avg2 - avg1

round_dif = round(dif / 130 * 13)

print(winner," ", 13,"-", 13 - round_dif," ", loser)

cur.close();
conn.close()

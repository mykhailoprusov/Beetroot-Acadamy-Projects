import psycopg2

# Я тут трохи пристосував завдання під свою таблицю. Сподіваюсь,
# це нічого

conn = psycopg2.connect(host="3.71.99.74",dbname = "mykhailo_homework1",
                        user = "postgres",password="RootBeet-101",
                         port = 5433
                                            )
cur = conn.cursor()

cur.execute("""SELECT name AS "Player name" FROM player_stats;""")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.execute("""SELECT DISTINCT position as "Player position" FROM player_stats;""")
positions = cur.fetchall()

print('---------------------------------------------')

for position in positions:
    print(position)

print('---------------------------------------------')

cur.execute("""SELECT * FROM player_stats ORDER BY name DESC ;""")
players = cur.fetchall()

for player in players:
    print(player)

print('---------------------------------------------')

cur.execute("""SELECT name, fifa_ranking FROM 
player_stats ORDER BY fifa_ranking;""")

name_and_fifa = cur.fetchall()

for info in name_and_fifa:
    print(info)

print('---------------------------------------------')

cur.execute("""SELECT MAX(fifa_ranking), MIN(fifa_ranking)
FROM player_stats;""")

fifa = cur.fetchone()


print(fifa)

print('---------------------------------------------')

cur.execute("""SELECT age FROM player_stats ORDER BY age;""")
ages = cur.fetchall()
print(ages)

conn.commit()

cur.close()
conn.close()
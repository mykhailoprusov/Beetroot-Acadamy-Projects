import psycopg2

conn = psycopg2.connect(host="3.71.99.74",dbname = "mykhailo_homework1",
                        user = "postgres",password="RootBeet-101",
                         port = 5433
                                            )
cur = conn.cursor()

# cur.execute("""CREATE TABLE players ( id INT PRIMARY KEY,
#             name VARCHAR(255),
#             age INT,
#             position VARCHAR(255),
#             fifa_ranking INT
#             );
#             """)

# cur.execute(""" ALTER TABLE players RENAME TO player_stats """)

# cur.execute("""ALTER TABLE player_stats ADD COLUMN club VARCHAR(255)""")



# cur.execute("""INSERT INTO player_stats (id,name, age, position, fifa_ranking, club) VALUES
#             (1,'Andriy Yarmolenko',32,'Forward',80,'West Ham United'),
#             (2,'Oleksandr Zinchenko',24,'Defender/Midfielder',80,'Manchester City'),
#             (3,'Roman Yaremchuk',26,'Forward',79,'Benfica'),
#             (4,'Mykola Shaparenko',23,'Midfielder',76,'Dynamo Kyiv'),
#             (5,'Vitaliy Mykolenko',22,'Defender',75,'Dynamo Kyiv');
#             """)


# cur.execute("""UPDATE player_stats SET age = 33 WHERE id =1;""")

# cur.execute("""INSERT INTO player_stats (id,name, age, position, fifa_ranking, club) VALUES
#                 (6,'Ruslan Malinovskyi',28,'Midfielder',80,'Atalanta')
#                 """)

# cur.execute("""DELETE FROM player_stats WHERE id = 6""")

# cur.execute("""INSERT INTO player_stats (id,name, age, position, fifa_ranking, club) VALUES
#             (6,'Viktor Tsygankov',23,'Midfielder',78,'Dynamo Kyiv'),
#             (7,'Denys Popov',22,'Defender',74,'Shakhtar Donetsk'),
#             (8,'Oleksandr Karavaev',26,'Defender',76,'Dynamo Kyiv'),
#             (9,'Bohdan Butko',30,'Defender',73,'Shakhtar Donetsk'),
#             (10,'Serhiy Sydorchuk',30,'Midfielder',75,'Dynamo Kyiv');
#             """)
conn.commit()

cur.close()
conn.close()
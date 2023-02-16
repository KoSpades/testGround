import psycopg2

conn = psycopg2.connect(database="kos",
                        host="localhost",
                        user="david",
                        password="",
                        port="5432")

cur = conn.cursor()

# cur.execute("CREATE USER david")
# cur.execute("GRANT SELECT ON payment TO david")
# cur.execute("CREATE VIEW low_income as SELECT * FROM payment WHERE salary <= 30")

cur.execute("SELECT * FROM low_income")

# cur.execute("GRANT SELECT ON low_income TO david")
print(cur.fetchall())
cur.close()
conn.commit()



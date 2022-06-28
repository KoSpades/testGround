import psycopg2

conn = psycopg2.connect(database="kos",
                        host="localhost",
                        user="kos",
                        password="",
                        port="5432")

cur = conn.cursor()

# cur.execute('''
#             CREATE TABLE payment (
#                 employee_id INTEGER PRIMARY KEY NOT NULL,
#                 salary INTEGER NOT NULL
#             );
#         ''')

cur.execute("""INSERT INTO payment(employee_id, salary) VALUES(3, 30);""")

cur.execute("SELECT * FROM payment")

print(cur.fetchall())

cur.close()

conn.commit()



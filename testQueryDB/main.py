import os
import sqlite3

def connect_to_db():
    conn = sqlite3.connect('testQueryDB/database.db')
    return conn

def create_info_table():
    try:
        conn = connect_to_db()
        conn.execute('''
            CREATE TABLE info (
                employee_id INTEGER PRIMARY KEY NOT NULL,
                email TEXT NOT NULL,
                department TEXT NOT NULL
            );
        ''')
        conn.commit()
        print("info table created successfully")
    except:
        print("info table creation failed")
    finally:
        conn.close()

def create_payment_table():
    try:
        conn = connect_to_db()
        conn.execute('''
            CREATE TABLE payment (
                employee_id INTEGER PRIMARY KEY NOT NULL,
                salary INTEGER NOT NULL
            );
        ''')
        conn.commit()
        print("payment table created successfully")
    except:
        print("payment table creation failed")
    finally:
        conn.close()

def insert_employee(e_info):
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO info (employee_id, email, department) VALUES (?, ?, ?)",
                    (e_info['employee_id'], e_info['email'], e_info['department']))
        conn.commit()
    except:
        conn().rollback()
    finally:
        conn.close()
    return 0

def insert_payment(e_pay):
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO payment (employee_id, salary) VALUES (?, ?)",
                    (e_pay['employee_id'], e_pay['salary']))
        conn.commit()
    except:
        conn().rollback()
    finally:
        conn.close()
    return 0

def create_view_no_cs():
    pass

def run_custom_query(query):
    conn = connect_to_db()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()

    # convert row objects to dictionary
    res = [dict(zip(row.keys(), row)) for row in rows]
    return res

def get_employee_info():
    query = "SELECT * FROM info"
    res = run_custom_query(query)
    return res

def get_employee_pay():
    query = "SELECT * FROM payment"
    res = run_custom_query(query)
    return res

def get_dept_avg_salary():
    query = "SELECT department, avg(salary) as dept_count FROM info, payment " \
            "WHERE info.employee_id = payment.employee_id GROUP BY department"
    res = run_custom_query(query)
    return res


e1 = {"employee_id": 1, "email": "david@gmail.com", "department": "math"}
e2 = {"employee_id": 2, "email": "jerry@gmail.com", "department": "cs"}
e3 = {"employee_id": 3, "email": "mike@gmail.com", "department": "math"}
e4 = {"employee_id": 4, "email": "lucy@gmail.com", "department": "math"}
e5 = {"employee_id": 5, "email": "ivan@gmail.com", "department": "cs"}
e6 = {"employee_id": 6, "email": "karissa@gmail.com", "department": "arts"}
e7 = {"employee_id": 7, "email": "jensen@gmail.com", "department": "arts"}
e8 = {"employee_id": 8, "email": "lina@gmail.com", "department": "arts"}

p1 = {"employee_id": 1, "salary": 1000}
p2 = {"employee_id": 2, "salary": 5000}
p3 = {"employee_id": 3, "salary": 2000}
p4 = {"employee_id": 4, "salary": 1500}
p5 = {"employee_id": 5, "salary": 9000}
p6 = {"employee_id": 6, "salary": 500}
p7 = {"employee_id": 7, "salary": 300}
p8 = {"employee_id": 8, "salary": 100}

if __name__ == "__main__":

    if os.path.exists("testQueryDB/database.db"):
        os.remove("testQueryDB/database.db")

    # Creating the tables
    create_info_table()
    create_payment_table()

    # Inserting the employees
    insert_employee(e1)
    insert_employee(e2)
    insert_employee(e3)
    insert_employee(e4)
    insert_employee(e5)
    insert_employee(e6)
    insert_employee(e7)
    insert_employee(e8)
    # Inserting the payments
    insert_payment(p1)
    insert_payment(p2)
    insert_payment(p3)
    insert_payment(p4)
    insert_payment(p5)
    insert_payment(p6)
    insert_payment(p7)
    insert_payment(p8)

    # TODO: let's write a query here to create a view that filters out CS from info table

    # Get the values
    info_res = get_employee_info()
    pay_res = get_employee_pay()
    dept_avg_salary_res = get_dept_avg_salary()

    print(info_res)
    print(pay_res)
    print(dept_avg_salary_res)

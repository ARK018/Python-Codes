import pymysql

db = pymysql.connect(host="localhost", user="root", password="Polaris@18", database="DB")
cursor = db.cursor()

cursor.execute("""
    CREATE TABLE Employee(         
        E_id INT AUTO_INCREMENT PRIMARY KEY,
        E_name VARCHAR(255),
        E_age INT,
        E_salary INT
    )
""")

num_rows = int(input("Enter no. of rows to insert : "))

for i in range(num_rows):
    print(f"Enter details of Employee {i+1} : ")
    E_name = input("Employee Name : ")
    E_age = int(input("Employee Age : "))
    E_salary = int(input("Employee Salary : "))

    cursor.execute("""
        INSERT INTO Employee(E_name, E_age, E_salary)
        VALUES(%s, %s, %s)
    """, (E_name, E_age, E_salary))

db.commit()

cursor.execute("SELECT * FROM Employee")
rows = cursor.fetchall()
for row in rows:
    print(row) 

cursor.close()
db.close()
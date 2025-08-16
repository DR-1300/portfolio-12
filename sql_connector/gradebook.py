import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mysql123',
    database='school'
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Gradebook(
    Rollno INT PRIMARY KEY,
    Name VARCHAR(100),
    Subject VARCHAR(100),
    Marks INT
)
""")

while True:
    print("\n1. Add Student\n2. Search Student\n3. Exit")
    choice = input("Choose option: ")
    if choice == '1':
        roll = int(input("Enter Roll number: "))
        name = input("Enter Name: ")
        subject = input("Enter Subject: ")
        marks = int(input("Enter Marks: "))
        query = "INSERT INTO Gradebook (Rollno, Name, Subject, Marks) VALUES (%s, %s, %s, %s)"
        values = (roll, name, subject, marks)
        cursor.execute(query, values)
        conn.commit()
        print("Student added successfully.")
    elif choice == '2':
        name = input("Enter student name to search: ")
        query = "SELECT * FROM Gradebook WHERE Name = %s"
        cursor.execute(query, (name,))
        result = cursor.fetchall()
        for row in result:
            print(row)

    else:
        break

cursor.close()
conn.close()
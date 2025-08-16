import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql123",  # Replace this with your MySQL root password
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS user_login")
cursor.execute("USE user_login")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username VARCHAR(50) PRIMARY KEY,
        password VARCHAR(50) NOT NULL
    )
""")


# Main menu
while True:
    print("\n--- User Login System ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = int(input("Enter an option: "))

    if choice == 1:
        username = input("Enter a username: ").strip()
        password = input("Enter a password: ").strip()
        try:
            cursor.execute("INSERT INTO users VALUES (%s, %s)", 
                           (username, password))
            db.commit()
            print("✅ Registration successful!")
        except mysql.connector.IntegrityError:
            print("⚠️ Username already exists. Try another.")
    elif choice == 2:
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()
        cursor.execute("SELECT * FROM users WHERE username = %s " \
        "AND password = %s", (username, password))
        user = cursor.fetchone()
        if user:
            print(f"Welcome {username}")
        else:
            print("❌ Invalid username or password.")
    elif choice == 3:
        print("👋 Exiting...")
        break
    else:
        print("❌ Invalid choice.")

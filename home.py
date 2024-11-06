import mysql.connector as mysql
import bcrypt
from dotenv import load_dotenv
import os

load_dotenv()


# Database connection
try:
    db = mysql.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_DATABASE')
    )
    cs = db.cursor()
except mysql.Error as e:
    print(f"Error connecting to MySQL: {e}")
    exit(1)

def verify_password(password, hashed_password):
    """
    Verify if the provided password matches the hashed password.
    
    Args:
        password (str): The plain text password.
        hashed_password (str): The hashed password.
    
    Returns:
        bool: True if the password matches, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def display_choice_menu():
    """
    Display the login choice menu and return the user's choice.
    
    Returns:
        int: The user's choice.
    """
    print()
    print("==============================================================")
    print("||                       LOGIN SCREEN                       ||")
    print("==============================================================")
    print("||                   1) Librarian Login                     ||")
    print("||                   2) Member Login                        ||")
    print("||                   3) Exit the program                    ||")
    print("==============================================================")
    print()
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return display_choice_menu()
    return choice

def librarian_login():
    """
    Handle the librarian login process.
    """
    print()
    username = input("Enter your username: ")
    password = input("Enter the password: ")
    cs.execute("SELECT hashed_password FROM logindata WHERE USERNAME = %s", (username,))
    result = cs.fetchone()
    if result is None:
        print("Username not found!")
    else:
        hashed_password = result[0]
        if verify_password(password, hashed_password):
            print("Login Successful!")
            from librarian import dashboardLibrarian
            dashboardLibrarian()
        else:
            print("Password Incorrect! Please try again!")

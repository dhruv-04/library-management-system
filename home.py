import mysql.connector as mysql

def main():
    db = mysql.connect(host="localhost", user="root", password="Dhruv471__01")
    if db.is_connected():
        print("Connection to server established!")
    else:
        print("Connection to server failed!")

if __name__ == "__main__":
    main()   
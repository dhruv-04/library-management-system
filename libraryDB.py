import mysql.connector as mysql
import string 
import random
from faker import Faker
import bcrypt

#create connection object
db = mysql.connect(host="localhost", user="root", password="Dhruv471__01") #connection object

def createHashedPassword(passwd):
    hashedPasswd = bcrypt.hashpw(passwd.encode('utf-8'), bcrypt.gensalt())
    return hashedPasswd

genreCode = {
    'Horror' : 'HR', 
    'Romantic' : 'RM',
    'Psychological thriller' : 'PT',
    'Mystery' : 'MS',
    'Fiction' : 'FC',
    'Biography' : 'BO',
    'Drama' : 'DA',
    'AutoBiography' : 'AB',
    'Children' : 'CD',
    'Poetry' : 'PE',
    'Crime' : 'CR'
}


#function to create fake data
def createFakeData():
    books = [
        ''.join(random.choices(string.ascii_letters + ' ', k = 20)),
        ''.join(random.choices(string.ascii_letters, k = 10)),
        ''.join(random.choices(string.ascii_letters + ' ', k = 10)),
        random.randint(1900, 2024),
        ''.join(random.choice(['Horror', 'Romantic', 'Psychological thriller', 'Mystery', 'Fiction', 'Biography',
                               'Drama', 'AutoBiography', 'Children', 'Poetry', 'Crime'])),
        ''.join(random.choice(['English', 'Hindi', 'Marathi', 'Gujrati', 'Spanish', 'French', 'Urdu', 'Dutch', 'German',
                               'Portugese', 'Japanese'])),
        random.randint(10,1000),
        random.randint(1,20)
    ]
    return books

def fakerFakeData():
    faker = Faker()
    return [
        faker.sentence(nb_words = 2),
        faker.first_name(),
        faker.company(),
        random.randint(1900, 2024),
        ''.join(random.choice(['Horror', 'Romantic', 'Psychological thriller', 'Mystery', 'Fiction', 'Biography',
                                'Drama', 'AutoBiography', 'Children', 'Poetry', 'Crime'])),
        ''.join(random.choice(['English', 'Hindi', 'Marathi', 'Gujrati', 'Spanish', 'French', 'Urdu', 'Dutch', 'German',
                               'Portugese', 'Japanese'])),      
        random.randint(10, 1000),
        random.randint(1,20)
    ]


#function to create bookID
def createBookID(genre, yearOfPublication, author):
    cs.execute('''SELECT LPAD(COUNT(Book_ID) + 1, 4, '0') FROM BOOKS WHERE AUTHOR = %s''', (author,))
    counter = cs.fetchone()[0]
    return genreCode[genre] + str(yearOfPublication) + author[0:2].upper() + counter


if db.is_connected():
    cs = db.cursor()  # cursor object
    print("Connection to the server established!")

    # check if the database already exists
    try:
        cs.execute("DROP DATABASE IF EXISTS library_management;")
        cs.execute("CREATE DATABASE library_management;")
        cs.execute("USE library_management;")

        cs.execute('''
            CREATE TABLE BOOKS (
                Book_ID VARCHAR(12) PRIMARY KEY,
                Title VARCHAR(255) NOT NULL,
                Author VARCHAR(255) NOT NULL,
                Publisher VARCHAR(255) NOT NULL,
                Year_Of_Publication INT NOT NULL,
                Category VARCHAR(255) NOT NULL,
                Language VARCHAR(255) NOT NULL,
                No_Of_Pages INT,
                No_Of_Copies INT NOT NULL
            );
        ''')
        print("Books table created successfully.")

        for i in range(100):
            if(i < 51):
                books = createFakeData()
                cs.execute('''INSERT INTO BOOKS(Book_ID, Title, Author, Publisher, Year_Of_Publication, Category, Language, No_Of_Pages, No_Of_Copies)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)''',(createBookID(books[4], books[3], books[1]), books[0], books[1], books[2], books[3], books[4],
                                                                    books[5], books[6], books[7]))
            else:
                books = fakerFakeData()
                cs.execute('''INSERT INTO BOOKS(Book_ID, Title, Author, Publisher, Year_Of_Publication, Category, Language, No_Of_Pages, No_Of_Copies)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)''',(createBookID(books[4], books[3], books[1]), books[0], books[1], books[2], books[3], books[4],
                                                                    books[5], books[6], books[7]))
        
        db.commit()
        print("Insertion of 100 books successful!")


        #creation of Login table
        cs.execute('''CREATE TABLE LOGINDATA(
                   Username VARCHAR(50) NOT NULL PRIMARY KEY,
                   Hashed_Password VARCHAR(60) NOT NULL,
                   Status VARCHAR(7) NOT NULL DEFAULT 'OFFLINE');''')
        
        passwd = 'librarian01'

        cs.execute('''INSERT INTO LOGINDATA VALUES(
                   'Librarian01', %s, 'OFFLINE');''', (createHashedPassword(passwd).decode(),))
        
        db.commit()

    except mysql.Error as e:
        print(e)

    finally:
        if db.is_connected():
            cs.close()
            db.close()

else:
    print("Connection to server unsuccessful!")
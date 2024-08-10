import mysql.connector as mysql
import string 
import random
from faker import Faker

#create connection object
db = mysql.connect(host="localhost", user="root", password="Dhruv471__01") #connection object


#function to create fake data
def createFakeData():
    books = [
        ''.join(random.choices(string.ascii_letters + ' ', k = 20)),
        ''.join(random.choices(string.ascii_letters + ' ', k = 10)),
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
        faker.name(),
        faker.company(),
        random.randint(1900, 2024),
        ''.join(random.choice(['Horror', 'Romantic', 'Psychological thriller', 'Mystery', 'Fiction', 'Biography',
                                'Drama', 'AutoBiography', 'Children', 'Poetry', 'Crime'])),
        faker.language_name(),       
        random.randint(10, 1000),
        random.randint(1,20)
    ]

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
                Book_ID INT AUTO_INCREMENT PRIMARY KEY,
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
                cs.execute('''INSERT INTO BOOKS(Title, Author, Publisher, Year_Of_Publication, Category, Language, No_Of_Pages, No_Of_Copies)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''',(books[0], books[1], books[2], books[3], books[4],
                                                                    books[5], books[6], books[7]))
            else:
                books = fakerFakeData()
                cs.execute('''INSERT INTO BOOKS(Title, Author, Publisher, Year_Of_Publication, Category, Language, No_Of_Pages, No_Of_Copies)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''',(books[0], books[1], books[2], books[3], books[4],
                                                                    books[5], books[6], books[7]))
        
        db.commit()
        print("Insertion of 200 books successful!")

    except mysql.Error as e:
        print(e)

    finally:
        if db.is_connected():
            cs.close()
            db.close()

else:
    print("Connection to server unsuccessful!")
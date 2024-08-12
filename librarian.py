import mysql.connector as mysql

try:
    db = mysql.connect(host="localhost", username="root", password="Dhruv471__01", database="library_management")
    cs = db.cursor()
except mysql.Error as e:
    print(e)



# funciton to add details in the books table in the database
def addDetails():
    print("Enter the title of the book : ", end="")
    title = input()

    print("Enter the author of the book : ", end="")
    author = input()

    print("Enter the publisher of the book : ", end="")
    publisher = input()

    #loop continues to execute until the right input is given
    yop = -1
    while True:
        try:
            print("Enter the year of publication (Numerical value) : ", end="")
            yop = int(input())
            break
        except ValueError:
            print("Enter the correct numerical value")
            print()


    print("Enter the genre of the book : ", end="")
    genre = input()

    print("Enter the language of the book : ", end="")
    language = input()

    #loop continues to execute until the right input is given
    pages = 0
    while True:
        try:
            print("Enter the number of pages (Numerical Value) : ", end="")
            pages = int(input())
            break
        except ValueError:
            print("Enter the correct numerical value!")
            print()

    #loop continues to execute until the right input is given
    copies = 0
    while True:
        try:
            print("Enter the number of copies (Numerical Value) : ", end="")
            copies = int(input())
            break
        except ValueError:
            print("Enter the correct numerical value!")
            print()

    #block to execute the insert operation in the books table
    try:
        cs.execute('''INSERT INTO books (Title, Author, Publisher, Year_Of_Publication, Category, Language, No_Of_Pages, No_Of_Copies) VALUES
               (%s, %s, %s, %s, %s, %s, %s, %s);''', (title, author, publisher, yop, genre, language, pages, copies))
        db.commit()
        print("Books details updated successfully!")
    except mysql.Error as e:
        print("Error while executing the insertion command!", e)
        db.rollback()


#function to return the choice of the user
def choice():
    try:
        print("Enter the choice : ", end="")
        ch = int(input())
    except ValueError:
        print("Invalid Input! Enter the correct number.")
        choice()
    
    match(ch):
        case 1:
            addDetails()
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            print("Logging You out....")
            from main import home_function
            home_function()
        case _:
            print("Enter the correct choice!")
            print()
            choice()

#function to show librarian dashboard option
def dashboardLibrarian():
    for i in range(5): print()
    print("=============================================================================================================")
    print("||                           **      **   ***********   **      *   *           *                          ||")
    print("||                           * *    * *   *             * *     *   *           *                          ||")
    print("||                           *  *  *  *   *             *  *    *   *           *                          ||")
    print("||                           *   **   *   *******       *   *   *   *           *                          ||")
    print("||                           *        *   *             *    *  *   *           *                          ||")
    print("||                           *        *   *             *     * *     *       *                            ||")
    print("||                           *        *   **********    *      **       *****                              ||")
    print("=============================================================================================================")
    print("|| 1) Enter the book details to be added.                                                                  ||")
    print("|| 2) Modify existing book information.                                                                    ||")
    print("|| 3) Search books by title, author, genre, publisher or year of publication.                              ||")
    print("|| 4) Add new member for membership.                                                                       ||")
    print("|| 5) Log out.                                                                                             ||")
    print("=============================================================================================================")
    choice()
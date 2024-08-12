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

#function to view books in a set of 20
def viewBooks():
    viewCursor = db.cursor()
    try:
        ch = 'yes'
        limit = 20
        offset = 0
        while ch == 'y' or ch == 'yes':
            viewCursor.execute("SELECT * FROM books LIMIT %s OFFSET %s;", (limit, offset)) #fetchmany was causing in error ""
            books = viewCursor.fetchall()
            if not books:
                print()
                print("No more books are available!")
                break
            else:
                print("{:<10} {:<30} {:<30} {:<40} {:<10} {:<30} {:<15} {:<10} {:<10}".format(
                    "Book No", "Title", "Author", "Publisher", "Year", "Genre", "Language", "Pages", "Copies"
                ))
                print("="*194)

                for i in books:
                    print("{:<10} {:<30} {:<30} {:<40} {:<10} {:<30} {:<15} {:<10} {:<10}".format(
                        i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]
                    ))
                    print()
                print("Do you want to view the next 20 books? Enter (y/n) : ", end="")
                ch = input().strip().lower()
                print()
                if ch == 'y' or ch == 'yes':
                    offset += limit
                else:
                    break
    except mysql.Error as err:
        print(f"Error: {err}")
    finally:
        # Ensure the cursor is closed
        if viewCursor:
            viewCursor.close()
    # Returns control to the dashboard
    dashboardLibrarian()


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
            viewBooks()
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
    print("|| 2) View the books and their availabilty inside the library.                                             ||")
    print("|| 2) Modify existing book information.                                                                    ||")
    print("|| 3) Search books by title, author, genre, publisher or year of publication.                              ||")
    print("|| 4) Add new member for membership.                                                                       ||")
    print("|| 5) Log out.                                                                                             ||")
    print("=============================================================================================================")
    choice()

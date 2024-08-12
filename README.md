# Library-Management-System
This is a Library Management Project which is being built in Python and the database support is given by MySql.
This project is still in development and further information will be updated along the way. The changes that been commited in this project are verified and working correctly, provided the configurations in the laptop are correct. This is currently a **TERMINAL UI** based project, it will further be developed to a proper GUI in the near future.

## Prerequisites
**ESSENTIAL SOFTWARES:**
  1) **Python** : 3.12 or higher. Download from : https://www.python.org/downloads/
  2) **MySql** : A Database management system for storing library data. Download from : https://dev.mysql.com/downloads/installer/
  3) **MySql connector** : This can be installed using the python command "pip install mysql-connector-python" in your cmd. If it says "pip command is not recognised". Follow the given guide to install pip and revert back to the original step : https://pip.pypa.io/en/stable/installation/
  4) **IDE** : To edit the python code.
**Note:** Ensure that Python is added to your system's PATH environment variable for easy command-line access.

## Implemented Features of the LMS
  1) **Librarian Dashboard** : A librarian dashbaord has been created with all the necessary functions that the librarian can perform. A single operation can be performed at the time. For now, the only function that has been fully implemented is the **addDetails** function, which allows the librarian to add the information about the new book in the database.
  2) **Hashing Password** : A hashing system has been implemented using bcrypt module in python to store the passwords in a secure manner in the database in order to follow the secure practices. (home.py)
  3) **Interactive Menu** : An interactive menu has been implemented so that the user can use it effectively just like it would have been in a GUI.
  4) **Error Handling** : All the functions that have been implemented, have right error handling mechanism in place in order to prevent any unwanted execution of the program.
  5) **Faker module** : Faker module has been used to provide 50 test data in the database, also a small script created by me has also been used in order to generate another 50 test data (total 100).



## How To Execute?
  1) Change the database username and password in all the files that are present in this repository to the username and password that you have on your system.
     Example : mycon = mysql.connect(host="localhost", user="your_username", password="your_password", database="library_management");
  2) **librarianDB.py** : Execute this file in order to create the required database and the tables associated with it.
  3) **main.py** : Execute this file, and the related function would be implemented automatically based on the choice of the user.


Thank you for trying the project. Future updates will be shared soon. Stay Tuned!

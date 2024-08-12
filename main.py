from home import librarian_login, display_choice_menu

def home_function():
    while True:
        choice = display_choice_menu()
        match choice:
            case 1:
                librarian_login()
            case 2:
                print("Member login not implemented yet.")
            case 3:
                print("Exiting the program.")
                exit()
            case _:
                print("Invalid choice. Please try again.")
            
home_function()
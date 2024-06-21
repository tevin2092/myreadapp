from src.db.models import reader

class MenuDisplay:
    @staticmethod
    def display_main_menu():
        print(
            """
        WELCOME TO MY READ APP

        MENU    
        -----------
        1. DATA MANIPULATION
        2. DATA QUERY
        00. QUIT
        """
        )

    @staticmethod
    def display_DM_menu():
        print(
            """
        1. INSERT READER
        2. INSERT BOOK
        3. INSERT MYREAD
        """
        )

def main():
    while True:
        MenuDisplay.display_main_menu()
        option: int = int(input('Choose an option to continue:'))

        if option == 1:
            MenuDisplay.display_DM_menu()
            option: int = int(input('Choose an option to continue:'))

            if option ==1:
            elif option == 2:
            pass
        elif option == 0:
            print('PROGRAM IS QUITTING')
            break
        else:
            print('Option not recognized. Please, try again')

if __name__ == '__main__':
    main()
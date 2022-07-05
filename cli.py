class MainMenu:

    def main_menu():
        print("Welcome to WGUPS Logistics. \n"
              "Please select from the following options:\n"
              "------------------------------\n"
              "1. View status of ALL Packages\n"
              "2. View status of SINGLE Package\n"
              "3. Exit WGUPS Logistics")
        user_choice = input("Selection: ")
        if user_choice == '1':
            print("All Package Status placeholder\n")
            MainMenu.main_menu()
        elif user_choice == '2':
            print("Single package status placeholder\n")
            MainMenu.main_menu()
        elif user_choice == '3':
            exit()
        else:
            print("Invalid Selection, please try again.\n")
            MainMenu.main_menu()

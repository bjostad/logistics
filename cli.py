# Bruce Bjostad Student ID:009839410

from package import hashed_packages

# Command Line Interface for the WGUPS logistics program
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
        main_menu()
    elif user_choice == '2':
        package_choice = input("What is the package ID you would like to track: ")
        print(hashed_packages.find_package(package_choice))
        hashed_packages.remove_package(package_choice)
        input("Press enter to return to menu.")
        main_menu()
    elif user_choice == '3':
        exit()
    else:
        print("Invalid Selection, please try again.\n")
        main_menu()


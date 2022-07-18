# Bruce Bjostad Student ID:009839410
import package
from logistics import collected_packages
from logistics import truck_reports

class Menu:

    def __init__(self):
        pass

    # Command Line Interface for the WGUPS logistics program
    def main_menu(self):
        print("Welcome to WGUPS Logistics. \n"
              "Please select from the following options:\n"
              "------------------------------\n"
              "1. View status of ALL Packages\n"
              "2. View status of SINGLE Package\n"
              "3. Exit WGUPS Logistics")
        user_choice = input("Selection: ")
        if user_choice == '1':
            self.all_status()
        elif user_choice == '2':
            self.single_status()
        elif user_choice == '3':
            exit()
        else:
            print("Invalid Selection, please try again.\n")
            self.main_menu()

    #Display the status of all packages
    #O(N)
    def all_status(self):
        print("Status of all packages")
        print("| {:<2} | {:^40} {:^16} {:<2} {:^5} | {:^15} | {:^22} |".format("#", "Address", "City", "St", "Zip",
                                                                               "Deadline", "Status"))
        for i in range(1, len(collected_packages) + 1):
            p = collected_packages.find_package(str(i))
            print("| {:<2} | {:^40} {:^16} {:<2} {:^5} | {:^15} | {:^22} |"
                  .format(p.id, p.address, p.city, p.st, p.zip, p.deadline, p.status))
        truck_reports()
        input("\nPress enter to return to menu.")
        self.main_menu()

    #Display the status of a single selected package
    #O(N)
    def single_status(self):
        package_choice = input("What is the package ID you would like to track: ")
        p = collected_packages.find_package(package_choice)
        print("| {:<2} | {:^40} {:^16} {:<2} {:^5} | {:^15} | {:^22} |".format("#", "Address", "City", "St", "Zip",
                                                                               "Deadline", "Status"))
        print("| {:<2} | {:^40} {:^16} {:<2} {:^5} | {:^15} | {:^22} |"
              .format(p.id, p.address, p.city, p.st, p.zip, p.deadline, p.status))
        input("Press enter to return to menu.")
        self.main_menu()
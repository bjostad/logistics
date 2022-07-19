# Bruce Bjostad Student ID:009839410

from datetime import timedelta
from dataimport import create_atlas
from dataimport import collect_packages
from truck import Truck


class Logistics:

    atlas = create_atlas()
    collected_packages = collect_packages()
    stop_time = timedelta(hours=8, minutes=00)
    truck1 = Truck(1, timedelta(hours=8, minutes=0), timedelta(hours=14, minutes=25), atlas)
    truck2 = Truck(2, timedelta(hours=9, minutes=5), timedelta(hours=14, minutes=25), atlas)
    truck3 = Truck(3, timedelta(hours=10, minutes=20), timedelta(hours=14, minutes=25), atlas)

    def __init__(self):
        pass

    # Set stop time for checking status at specific times
    # O(1)
    def set_stop_time(self):
        selected_stop_time = input("What time is it? (hh:mm)")
        hours, minutes = map(int, selected_stop_time.split(':'))
        fixed_stop_time = timedelta(hours=hours, minutes=minutes)
        return fixed_stop_time

    # Load Truck with packages
    # Accept list of package ids
    # Lookup package by id and load into truck
    # O(N)
    def load_truck(self, truck: Truck, manifest: list):
        for id in manifest:
            truck.load_package(self.collected_packages.find_package(id))

    # Begin the delivery day for WGUPS
    # O(N^2)
    def deliver(self):

        # Truck package manifest as determined by the WGUPS Hub
        first_load_manifest = [1, 5, 8, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 39, 40]
        second_load_manifest = [3, 6, 18, 25, 28, 32, 36, 38, 26, 4, 17, 21, 11, 23, 24, 22]
        third_load_manifest = [9, 2, 33, 7, 10, 27, 35, 12]

        # Set trucks stop time to specified time
        stop_time = self.set_stop_time()
        truck1 = Truck(1, timedelta(hours=8, minutes=0), stop_time, self.atlas)
        truck2 = Truck(2, timedelta(hours=9, minutes=5), stop_time, self.atlas)
        truck3 = Truck(3, timedelta(hours=10, minutes=20), stop_time, self.atlas)

        # Load and begin deliveries for Truck 1
        self.load_truck(truck1, first_load_manifest)
        truck1.run_route()

        # Load and begin deliveries for Truck 2
        self.load_truck(truck2, second_load_manifest)
        truck2.run_route()

        # Return Truck 1 to the hub so the driver can take Truck 3
        truck1.return_to_hub()

        # Load and begin deliveries for Truck 3
        self.load_truck(truck3, third_load_manifest)
        truck3.run_route()

        # Output truck reports at the end of the day
        self.truck_reports(truck1, truck2, truck3)
        self.truck_totals(truck1, truck2, truck3)

    # Individual truck reports
    # O(1)
    def truck_reports(self, truck1, truck2, truck3):
        truck1.truck_report()
        truck2.truck_report()
        truck3.truck_report()

    # Combined Truck Totals report
    # O(1)
    def truck_totals(self, truck1, truck2, truck3):
        all_truck_total_time = truck1.total_delivery_time + truck2.total_delivery_time + truck3.total_delivery_time
        all_trucks_total_distance = truck1.total_distance + truck2.total_distance + truck3.total_distance
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= Trucks Total "
              "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("Total Time: " + str(all_truck_total_time) + "     |    Total Distance Traveled: "
              + str(all_trucks_total_distance) + " miles")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- "
              "STATUS OF ALL PACKAGES =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

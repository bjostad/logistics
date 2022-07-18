# Bruce Bjostad Student ID:009839410

from datetime import timedelta
from dataimport import create_atlas
from dataimport import collect_packages
from truck import Truck

collected_packages = collect_packages()
atlas = create_atlas()

first_load_manifest = [1,5,8,13,14,15,16,19,20,29,30,31,34,37,39,40]
second_load_manifest = [3,6,18,25,28,32,36,38,26,4,17,21,11,23]
third_load_manifest = [9,2,33,7,10,27,35]
fourth_load_manifest = [24,22,12]

# first_load_manifest = [2,4,7,13,14,15,16,17,19,27,29,31,33,34,35,40]
# second_load_manifest = [3,5,6,8,9,18,24,25,28,30,31,32,36,37,38]
# third_load_manifest = [1,39]
#


truck1 = Truck(1, timedelta(hours=8, minutes=0), timedelta(hours=11, minutes=00), atlas)
truck2 = Truck(2, timedelta(hours=9, minutes=5), timedelta(hours=17, minutes=00), atlas)
truck3 = Truck(3, timedelta(hours=10, minutes=25), timedelta(hours=20, minutes=00), atlas)

def load_truck(truck: Truck, manifest: list):
    for id in manifest:
        truck.load_package(collected_packages.find_package(id))


load_truck(truck1, first_load_manifest)
truck1.run_route()

load_truck(truck2, second_load_manifest)
truck2.run_route()

truck1.return_to_hub()
truck2.return_to_hub()

package9 = collected_packages.find_package(9)
package9.update_address("410 S State St")


load_truck(truck3, third_load_manifest)
truck3.run_route()
load_truck(truck2, fourth_load_manifest)
truck2.run_route()

def truck_reports():
    truck1.truck_report()
    truck2.truck_report()
    truck3.truck_report()



# testing packages and deliveries
# pkg1 = hashed_packages.find_package(1)
# pkg13 = hashed_packages.find_package(13)
# pkg23 = hashed_packages.find_package(23)
# pkg33 = hashed_packages.find_package(33)
#
# truck1 = Truck(1, timedelta(hours=9, minutes=0))
# truck1.load_package(pkg1)
# truck1.load_package(pkg13)
# truck1.load_package(pkg23)
# truck1.load_package(pkg33)
# truck1.deliver_package(pkg13, atlas.get_distance(truck1.current_location, pkg13.address))
# truck1.deliver_package(pkg23, atlas.get_distance(truck1.current_location, pkg23.address))
# truck1.deliver_package(pkg33, atlas.get_distance(truck1.current_location, pkg33.address))
#
# print(truck1)


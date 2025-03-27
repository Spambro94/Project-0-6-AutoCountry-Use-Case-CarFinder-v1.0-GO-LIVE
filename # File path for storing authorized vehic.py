# File path for storing authorized vehicles
VEHICLE_FILE = "authorized_vehicles.txt"

def load_vehicles():
    
    try:
        with open(VEHICLE_FILE, 'r') as file:
            vehicles = [line.strip() for line in file.readlines()]
        return vehicles
    except FileNotFoundError:
        # If the file doesn't exist, return an empty list
        return []

def save_vehicles(vehicles):
    
    with open(VEHICLE_FILE, 'w') as file:
        for vehicle in vehicles:
            file.write(vehicle + "\n")

def print_menu():
    
    print("********************************")
    print("AutoCountry Vehicle Finder v0.5")
    print("********************************")
    print("Please Enter the following number below from the following menu:\n")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")
    print("********************************")

def print_all_vehicles(vehicles):
   
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
    if vehicles:
        for vehicle in vehicles:
            print(vehicle)
    else:
        print("No authorized vehicles available.")

def search_vehicle(vehicles):
    """Search for an authorized vehicle."""
    vehicle_name = input("\nPlease Enter the full Vehicle name: ").strip()
    if vehicle_name in vehicles:
        print(f"\n{vehicle_name} is an authorized vehicle")
    else:
        print(f"\n{vehicle_name} is not an authorized vehicle, if you received this in error please check the spelling and try again")

def add_vehicle(vehicles):
    
    new_vehicle = input("\nPlease Enter the full Vehicle name you would like to add: ").strip()
    vehicles.append(new_vehicle)
    save_vehicles(vehicles)
    print(f"\nYou have added \"{new_vehicle}\" as an authorized vehicle")

def delete_vehicle(vehicles):
  
    vehicle_name = input("\nPlease Enter the full Vehicle name you would like to REMOVE: ").strip()

    if vehicle_name in vehicles:
        confirmation = input(f"\nAre you sure you want to remove \"{vehicle_name}\" from the Authorized Vehicles List? (yes/no): ").strip().lower()

        if confirmation == "yes":
            vehicles.remove(vehicle_name)
            save_vehicles(vehicles)
            print(f"\nYou have REMOVED \"{vehicle_name}\" as an authorized vehicle")
        else:
            print("\nRemoval cancelled.")
    else:
        print(f"\n{vehicle_name} is not in the Authorized Vehicles List, please check the name and try again.")

def main():
    
    vehicles = load_vehicles()

    while True:
        print_menu()
        user_input = input("Enter your choice: ")

        if user_input == "1":
            print_all_vehicles(vehicles)
        elif user_input == "2":
            search_vehicle(vehicles)
        elif user_input == "3":
            add_vehicle(vehicles)
        elif user_input == "4":
            delete_vehicle(vehicles)
        elif user_input == "5":
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid input, please try again.")

# Running the program
if __name__ == "__main__":
    main()
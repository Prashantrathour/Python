import json
print("--------------------------------------------------------")
print("------            Mumbai Munchies               --------")
print("--------------------------------------------------------")
def load_inventory():
    try:
        with open("inventory.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_inventory(snack):
    try:
        with open("inventory.json", "w") as file:
            json.dump(snack, file)
    except IOError:
        print("Error: Unable to save inventory data.")

def operation_1(snack):
    try:
        ID = input("Enter Id: ")
        name = input("Enter snack name: ")
        price = input("Enter snack price: ")
        availability = input("Enter snack availability (yes/no): ")
        if ID and name and price:
            snack.append({"name": name, "ID": ID, "price": price, "availability": availability})
            print("Snack successfully added to database")
            save_inventory(snack)  # Save the updated inventory to the JSON file
        else:
            print("Please enter all fields")
    except Exception as e:
        print("An error occurred:", e)

def operation_2(snack):
    try:
        ID = input("Enter Id: ")
        for item in snack:
            if item["ID"] == ID:
                snack.remove(item)
                print("Snack successfully removed from the database")
                save_inventory(snack)  # Save the updated inventory to the JSON file
                return
        print("Invalid ID")
    except Exception as e:
        print("An error occurred:", e)

def operation_4(snack):
    try:
        ID = input("Enter Id: ")
        for item in snack:
            if item["ID"] == ID:
                print("Existing Snack Details:")
                print(f"ID: {item['ID']}")
                print(f"Name: {item['name']}")
                print(f"Price: {item['price']}")
                print(f"Availability: {item['availability']}")

                name = input("Enter new snack name (press enter to keep the same): ")
                price = input("Enter new snack price (press enter to keep the same): ")
                availability = input("Enter new snack availability (yes/no) (press enter to keep the same): ")

                if name:
                    item["name"] = name
                if price:
                    item["price"] = price
                if availability:
                    item["availability"] = availability

                print("Snack successfully updated in the database")
                save_inventory(snack)  # Save the updated inventory to the JSON file
                return

        print("Invalid ID")
    except Exception as e:
        print("An error occurred:", e)

def selsnack(snack):
    try:
        ID = input("Enter Id: ")
        for item in snack:
            if item["ID"] == ID and item["availability"] == "yes":
                snack.remove(item)
                print("Snack sold")
                save_inventory(snack)  # Save the updated inventory to the JSON file
                return item["price"]

        print("Invalid ID or not Available")
    except Exception as e:
        print("An error occurred:", e)
        return None

def available_snack(snack):
    try:
        available_snacks = [item for item in snack if item["availability"] == "yes"]
        if not available_snacks:
            print("No available snacks.")
        else:
            print("------------------------ All Available Snacks ----------------------------- ")
            for item in available_snacks:
                print(f"ID: {item['ID']}, Name: {item['name']}, Price: {item['price']}")
            print("---------------------------------------------------------------- ")
        return available_snacks
    except Exception as e:
        print("An error occurred:", e)
        return []

def main():
    snack = load_inventory()
    sell = {}
    count = 0
    price = 0

    while True:
        try:
            print("---------------------------------------------------------------- ")
            print("1. Add a snack to the inventory")
            print("2. Remove a snack from the inventory")
            print("3. Show all snacks")
            print("4. Update snack in the inventory")
            print("5. Sell snack")
            print("6. All available snack items")
            print("7. Total sell")
            print("8. Exit")
            print("---------------------------------------------------------------- ")

            operation = input("Enter your choice (1-8): ")

            if operation == "1":
                operation_1(snack)
            elif operation == "2":
                operation_2(snack)
            elif operation == "3":
                if not snack:
                    print("No inventory available. Please add inventory.")
                else:
                    print("--------------------------- All Snacks --------------------------------")
                    for item in snack:
                        print(f"ID: {item['ID']}, Name: {item['name']}, Price: {item['price']}, Availability: {item['availability']}")
                    print("-----------------------------------------------------------------------")

            elif operation == "4":
                operation_4(snack)
            elif operation == "7":
                print("------------- Sell Data --------------------")
                print(f"Total Price: {price}, Total Sell items: {count}")
            elif operation == "5":
                snack_price = selsnack(snack)
                if snack_price is not None:
                    price += int(snack_price)
                    count += 1
                    sell["totalPrice"] = price
                    sell["totalItem"] = count
            elif operation == "6":
                available_snack(snack)
            elif operation == "8":
                print("Thanks for visiting")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()

print("--------------------------------------------------------")
print("------ Zomato Chronicles: The Great Food Fiasco --------")
print("--------------------------------------------------------")


def add_dish_to_menu(menu):
    dish_id = len(menu) + 1
    dish_name = input("Enter the dish name: ")
    dish_price = float(input("Enter the dish price: "))
    dish_availability = input(
        "Is the dish available? (yes/no): ").lower() == 'yes'

    menu[dish_id] = {
        "name": dish_name,
        "price": dish_price,
        "availability": dish_availability
    }


def take_order(menu, orders):
    customer_name = input("Enter customer's name: ")

    # Handling input for dish IDs
    while True:
        dish_ids_input = input("Enter dish IDs (comma-separated) the customer wants to order: ")
        try:
            dish_ids = [int(dish_id.strip()) for dish_id in dish_ids_input.split(',')]
            break
        except ValueError:
            print("Invalid input. Please enter valid dish IDs separated by commas.")

    order_id = len(orders) + 1
    order_status = "received"

    order_dishes = []
    for dish_id in dish_ids:
        if dish_id in menu and menu[dish_id]["availability"]:
            order_dishes.append(dish_id)
        else:
            print(f"Dish with ID {dish_id} is not available. Order cannot be processed.")
            return

    orders[order_id] = {
        "customer_name": customer_name,
        "dishes": order_dishes,
        "status": order_status
    }

    print(f"Order received. Order ID: {order_id}")


def update_order_status(orders):
    order_id = int(input("Enter the order ID to update status: "))

    if order_id in orders:
        new_status = input(
            "Enter the new status ('preparing', 'ready for pickup', 'delivered'): ").lower()

        
        if new_status in ['preparing', 'ready for pickup', 'delivered']:
            orders[order_id]['status'] = new_status
            print("Order status updated successfully.")
        else:
            print("Invalid status. Please enter a valid status.")
    else:
        print("Invalid order ID. Order not found.")


def remove_dish_from_menu(menu):
    dish_id = int(input("Enter the dish ID to remove: "))
    menu.pop(dish_id, None)


def show_all_orders(orders):
    if not orders:
        print("No orders found.")
    else:
        print("--------------------------------------------------------")
        print("All Orders:")
        for order_id, order_info in orders.items():
            print(f"Order ID: {order_id}")
            print(f"Customer Name: {order_info['customer_name']}")
            print(
                f"Dish IDs: {', '.join(str(dish_id) for dish_id in order_info['dishes'])}")
            print(f"Status: {order_info['status']}")
            print()
        print("--------------------------------------------------------")    


def update_dish_availability(menu):
    dish_id = int(input("Enter the dish ID to update availability: "))
    if dish_id in menu:
        new_availability = input(
            "Is the dish available now? (yes/no): ").lower() == 'yes'
        menu[dish_id]['availability'] = new_availability
        print("--------------------------------------------------------")

        print("Availability updated successfully.")
        print("--------------------------------------------------------")
    else:
        print("Invalid dish ID. Dish not found in the menu.")


def main():

    print("Welcome to Zomato Chronicles: The Great Food Fiasco!")

    orders = {}
    menu = {
        1: {
            "name": "Pizza",
            "price": 12.99,
            "availability": True
        },
        2: {
            "name": "Burger",
            "price": 8.99,
            "availability": False
        },

    }
    while True:
        print("--------------------------------------------------------")
        print("\n1. Add dish to menu")
        print("2. Show menu")
        print("3. remove dish from menu")
        print("4. update dish availability")
        print("5. Take order")
        print("6. Show All orders")
        print("7. Update order status")
        print("8. Exit")
        print("--------------------------------------------------------")
        choice = int(input("Enter your choice (1-8): "))
        if choice == 1:
            add_dish_to_menu(menu)
        elif choice == 2:
            print("--------------------------------------------------------")
            print("Menu:")
            for dish_id, dish_info in menu.items():
                print(
                    f"{dish_id}. {dish_info['name']} - ${dish_info['price']:.2f} ({'Available' if dish_info['availability'] else 'Not Available'})")
            print("--------------------------------------------------------")    
        elif choice == 3:
            remove_dish_from_menu(menu)
            print("--------------------------------------------------------")
            print("Delete dish from menu")
            print("--------------------------------------------------------")
        elif choice == 4:
            update_dish_availability(menu)
        elif choice == 5:
            take_order(menu, orders)
        elif choice == 6:
            show_all_orders(orders)
        elif choice == 7:
            update_order_status(orders)    

        elif choice == 8:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()

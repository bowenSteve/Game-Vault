# lib/cli.py

from helpers import (
    create_customer,
    insert_customer,
    list_customers,
    delete_customer,
    update_customer,
    customer_orders,
    find_customer_name,
    create_game,
    Insert_game,
    delete_Game,
    update_Game,
    games_orders,
    find_game_publisher,
    find_game_name,
    list_all_games,
    create_order,
    insert_order,
    list_all_orders,
    update_order,
    delete_order,
    find_order_id,
    create_details,
    insert_order_details,
    list_order_details,
    delete_order_detail,
    update_Details,
    find_details_id
)


def main():
    while True:
        menu()
        choice = input("> ")
        #game menu
        if choice == "0":
            game_menu()
            game_input=input("> ")
            if game_input=="0":
                create_game()
            elif game_input=="1":
                Insert_game()
            elif game_input=="2":
                update_Game()
            elif game_input=="3":
                delete_Game()
            elif game_input=="4":
                find_game_name()
            elif game_input=="5":
                find_game_publisher()
            elif game_input=="6":
                list_all_games()
            elif game_input=="7":
                games_orders()
            elif game_input=="8":
                game_menu()
            elif game_input=="9":
                break
            else:
                print("Enter a valid input")
        #customer menu
        elif choice=="1":
            customer_menu()
            customer_input=input("> ")
            if customer_input=="0":
                create_customer()
            elif customer_input=="1":
                insert_customer()
            elif customer_input=="2":
                update_customer()
            elif customer_input=="3":
                delete_customer()
            elif customer_input=="4":
                find_customer_name()
            elif customer_input=="5":
                list_customers()
            elif customer_input=="6":
                customer_orders()
            elif customer_input=="7":
                game_menu()
            elif customer_input=="8":
                break
            else:
                print("Enter a valid input")


        #orders menu
        elif choice == "2":
            orders_menu()
            order_input=input("> ")
            if order_input=="0":
                create_order()
            elif order_input=="1":
                insert_order()
            elif order_input=="2":
                update_order()
            elif order_input=="3":
                delete_order()
            elif order_input=="4":
                find_order_id()
            elif order_input=="5":
                list_all_orders()
            elif order_input=="6":
                game_menu()
            elif order_input=="7":
                break
            else:
                print("Invalid input! Try again")
        #oder details menu
        elif choice=="3":
            order_details_menu()
            detail_input=input("> ")
            if detail_input=="0":
                create_details()
            elif detail_input=="1":
                insert_order_details()
            elif detail_input=="2":
                update_Details()
            elif detail_input=="3":
                delete_order_detail()
            elif detail_input=="4":
                find_details_id()
            elif detail_input=="5":
                list_order_details()
            elif detail_input=="6":
                game_menu()
            elif detail_input=="7":
                break
            else:
                print("Invalid input! Try again")
        
        elif choice=="4":
            break
        else:
            print("Invalid choice")


def menu():
    print("Welcome to Game-Vault gaming store")
    print("Please select an option:")
    print("0. Manage Games")
    print("1. Manage Customers")
    print("2. Manage Orders")
    print("3. Manage Order details")
    print("4. Exit")
def game_menu():
    print("Select an option:")
    print("0. Create Game")
    print("1. Add a new game")
    print("2. Update a game")
    print("3. Delete a game")
    print("4. Find a game by name")
    print("5. Find a game by the publisher's name")
    print("6. View all the games in store")
    print("7. View all the games with their orders")
    print("8. Back")
    print("9. Exit")
def orders_menu():
    print("Select an option:")
    print("0. Create Orders")
    print("1. Add a new order")
    print("2. Modify an existing order")
    print("3. Delete an order ")
    print("4. Find an order by ID")
    print("5. View all the orders")
    print("6. Back")
    print("7. Exit")
def customer_menu():
    print("Select an Option")
    print("0. Create Customer")
    print("1. Add a new customer")
    print("2. Update an existing customer")
    print("3. Delete a customer")
    print("4. Find a customer by name")
    print("5. View all the customers")
    print("6. View all the customers' orders")
    print("7. Back")
    print("8. Exit")
def order_details_menu():
    print("Select an Option")
    print("0. Create Order details")
    print("1. Add a new Order detail")
    print("2. Update an order detail")
    print("3. Delete an order detail")
    print("4. Find an order detail by ID")
    print("5. View all the order details")
    print("6. Back")
    print("7. Exit")
if __name__ == "__main__":
    main()

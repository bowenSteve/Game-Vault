# lib/cli.py

from helpers import (
    create_customer,
    insert_customer,
    list_customers,
    delete_customer,
    update_customer,
    customer_orders,
    create_game,
    Insert_game,
    delete_Game,
    update_Game,
    games_orders,
    list_all_games,
    create_order,
    insert_order,
    list_all_orders,
    update_order,
    delete_order,
    create_details,
    insert_order_details,
    list_order_details,
    delete_order_detail,
    update_Details
)


def main():
    while True:
        menu()
        choice = input("> ")
        #game menu
        if choice == "0":
            game_menu()
            game_input=input("> ")
            if game_input=="1":
                list_all_games()
            elif game_input=="2":
                Insert_game()
            elif game_input=="3":
                delete_Game()
            elif game_input=="4":
                update_Game()
            elif game_input=="5":
                games_orders()
            elif game_input=="6":
                game_menu()
            elif game_input=="7":
                break
            else:
                print("Enter a valid input")
        #customer menu
        elif choice=="1":
            customer_menu()
            customer_input=input("> ")
            if customer_input=="1":
                list_customers()
            elif customer_input=="2":
                insert_customer()
            elif customer_input=="3":
                delete_customer()
            elif customer_input=="4":
                update_customer()
            elif customer_input=="5":
                customer_orders()
            elif customer_input=="6":
                game_menu()
            elif customer_input=="7":
                break
            else:
                print("Enter a valid input")


        #orders menu
        elif choice == "2":
            orders_menu()
            order_input=input("> ")
            if order_input=="1":
                list_all_orders()
            elif order_input=="2":
                insert_order()
            elif order_input=="3":
                update_order()
            elif order_input=="4":
                delete_order()
            elif order_input=="5":
                game_menu()
            elif order_input=="6":
                break
            else:
                print("Invalid input! Try again")
        #oder details menu
        elif choice=="3":
            order_details_menu()
            detail_input=input("> ")
            if detail_input=="1":
                list_order_details()
            elif detail_input=="2":
                insert_order_details()
            elif detail_input=="3":
                delete_order_detail()
            elif detail_input=="4":
                update_Details()
            elif detail_input=="5":
                game_menu()
            elif detail_input=="6":
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
    print("1. Check all the games in store")
    print("2. Add a new game")
    print("3. Delete a game")
    print("4. update a game")
    print("5. Check all the games with their orders")
    print("6. Back")
    print("7. Exit")
def orders_menu():
    print("Select an option:")
    print("1. Check all the orders")
    print("2. Add a new order")
    print("3. Modify an order")
    print("4. Delete an order")
    print("5. Back")
    print("6. Exit")
def customer_menu():
    print("Select an Option")
    print("1. View all the customers")
    print("2. Add a new customer")
    print("3. Delete a customer")
    print("4. Update a customer")
    print("5. View all the customers' orders")
    print("6. Back")
    print("7. Exit")
def order_details_menu():
    print("Select an Option")
    print("1. View all the order details")
    print("2. Add a new order detail")
    print("3. Delete an order detail")
    print("4. Update an order detail")
    print("5. Back")
    print("6. Exit")
if __name__ == "__main__":
    main()

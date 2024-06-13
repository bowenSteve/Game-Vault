# lib/helpers.py

from models.customer import Customer
from models.game import Game
from models.publisher import Publisher
from models.order import Order
from models.orderdetails import Order_details

#customer_methods
def list_customers():
    customers = Customer.get_all()
    for customer in customers:
        print(customer)

def create_customer():
    Customer.create_table()

def insert_customer():
    name = input("Enter the customer's name: ")
    email = input("Enter the customer's email: ")
    if Customer.create(name, email):
        print("Customer added successfully!")
    else:
        print("Failed to add customer")

def delete_customer():
    cust_id = int(input("Enter the ID for the Customer to be deleted!: "))
    customer = Customer.find_by_id(cust_id)
    if customer:
        customer.delete()
        print("Customer deleted successfully!")
    else:
        print("Customer not found")

def update_customer():
    cust_id = input("Enter the ID of the customer you want to update: ")
    customer = Customer.find_by_id(cust_id)
    if customer:
        new_name = input("Enter the name of the Customer: ")
        new_email = input("Enter the Customer Email: ")
        customer.name = new_name
        customer.email = new_email
        customer.update()
        print("Customer updated successfully!")
    else:
        print("Customer not found!")


def customer_orders():
    Customer.customer_orders()

def find_customer_name():
    name = input("Enter the customer's name to search: ")
    customer = Customer.find_by_name(name)
    if customer:
        print(f"Customer: {customer}")
    else:
        print(f"Customer with name '{name}' not found.")


#game_methods
def create_game():
    Game.create_table()
def Insert_game():
    name=input("Enter the name of the game: ")
    price=float(input("Enter the price of the game: "))
    publisher=input("Enter the game publisher: ")
    Game.create(name, price, publisher)
    print("Game has been added successfully!")

def update_Game():
    game_id = input("Enter the ID of the game you want to update: ")
    game = Game.find_by_id(game_id)
    if game:
        new_name = input("Enter the new name of the game: ")
        new_price = float(input("Enter the new price of the game: "))
        new_publisher = input("Enter the new game publisher: ")
        game.name = new_name
        game.price = new_price
        game.publisher = new_publisher

        game.update()

        print("Game updated successfully!")
    else:
        print("Game not found!")

def list_all_games():
    games = Game.get_all()
    for game in games:
        print(game)
def delete_Game():
    game_id = int(input("Enter the ID for the game to be deleted!: "))
    game = Game.find_by_id(game_id)
    if game:
        game.delete()
        print("Game deleted successfully!")
    else:
        print("Game not found")
def games_orders():
    games = Game.games_with_orders()
    for game_order in games:
        print(game_order)
def find_game_name():
    name = input("Enter the Game name to search: ")
    game = Game.find_by_name(name)
    if game:
        print(f"Game: {game}")
    else:
        print(f"Game with name '{game}' not found.")

def find_game_publisher():
    publisher = input("Enter the Publisher's name: ")
    game = Game.find_by_publisher(publisher)
    if game:
        print(f"Game found: {game}")
    else:
        print(f"Game with publisher '{publisher}' not found.")

#order_methods
def create_order():
    Order.create_table()
def insert_order():
    game_ID=input("Enter the game ID: ")
    customer_ID=input("Enter the customer ID: ")
    date=input("Enter the date: ")
    Order.create(game_ID, customer_ID, date)
    print("Order added successfully!")
def list_all_orders():
    orders = Order.get_all()
    for order in orders:
        print(order)

def update_order():
    order_id = input("Enter the ID of the Order you want to update: ")
    order = Order.find_by_id(order_id)
    if order:
        game_ID = int(input("Enter the new game ID: "))
        customer_ID = int(input("Enter the new customer ID: "))
        date = input("Enter the new date: ")
        order.game_ID = game_ID
        order.customer_ID = customer_ID
        order.date = date

        order.update()

        print("Order updated successfully!")
    else:
        print("Order not found!")
def delete_order():
    order_id = int(input("Enter the ID for the Order to be deleted!: "))
    order = Order.find_by_id(order_id)
    if order:
        order.delete()
        print("Order deleted successfully!")
    else:
        print("Order not found")
def find_order_id():
    order_id=int(input("Enter the id for the order: "))
    order= Order.find_by_id(order_id)
    if order:
        print(f"Order: {order}")
    else:
        print("Order not found!")


#order details methods:
def create_details():
    Order_details.create_table()
def insert_order_details():
    OrderID=input("Enter the Order id: ")
    GameID=input("Enter the game id: ")
    quantity=int(input("Enter the quantity: "))
    Order_details.create(OrderID, GameID, quantity)
    print("Order details added successfully!")
def list_order_details():
    order_details = Order_details.get_all()
    for order_detail in order_details:
        print(order_detail)

def delete_order_detail():
    order_detail_id = int(input("Enter the ID for the Order detail to be deleted!: "))
    order_detail = Order_details.find_by_id(order_detail_id)
    if order_detail:
        order_detail.delete()
        print("Order detail deleted successfully!")
    else:
        print("Order detail not found")

def update_Details():
    order_detail_id = int(input("Enter the ID of the order detail you want to update: "))
    order_detail = Order_details.find_by_id(order_detail_id)
    if order_detail:
        order_ID = int(input("Enter the order ID: "))
        game_ID = int(input("Enter the game ID: "))
        quantity=int(input("Enter the quantity: "))
        order_detail.order_id = order_ID
        order_detail.game_id = game_ID
        order_detail.quantity=quantity

        order_detail.update()

        print("Order detail updated successfully!")
    else:
        print("Order detail not found!")
    
def find_details_id():
    detail_id=int(input("Enter the id for the order detail: "))
    detail= Order_details.find_by_id(detail_id)
    if detail:
        print(f"Order detail: {detail}")
    else:
        print("Order detail not found!")
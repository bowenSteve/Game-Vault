# Game-Vault

## Learning Goals

## Introduction
Game-Vault is a CLI application that can be used to manage a gaming store. It incoporates object-relational mapping and sqlite3 to create a table for customers, 
the games available in store, the orders and also a table for the order details. The application provides a robust system for managing store data efficiently and accurately through CRUD operations.

## Description
This application uses Python 3 as the object-oriented programming language, with its classes and attributes mapped to tables and columns respectively. 4 tables are going to be created in the database, these tables will belong to the classes Game, Customer, Order and OrderDetails.

- Game Class/Table: Represents games available in the store, storing attributes such as name, price, and publisher. Ensures data integrity through validations for price and name.

- Customers Class/Table: Manages customer information with attributes for name and email. Includes email validation and ensures each customer has a unique identifier.

- Order Class/Table: Tracks orders made by customers, associating each order with a specific game and customer through foreign keys. Stores the date of the order.

- Order Details Class/Table: Stores details of each order, including the quantity of each game ordered. Maintains referential integrity with orders and games through foreign keys.

### Relationships:
#### Many-to-Many Relationship:
OrderDetails Class/Table: This class/table represents a many-to-many relationship between orders and games. It connects orders to multiple games through the OrderID and GameID foreign keys, allowing multiple games to be associated with a single order and vice versa.
#### One-to-Many Relationships:
Order Class/Table: This class/table represents a one-to-many relationship between customers and orders. Each customer can place multiple orders, but each order belongs to exactly one customer, established through the customer_ID foreign key.
Customer Class/Table: This class/table also represents a one-to-many relationship between customers and orders. Each customer can place multiple orders, but each order belongs to exactly one customer, established through the customer_ID foreign key.

## Requirements
In order to run  this application, you need to have the following installed in your system:
--- Python3
--- sqlite3
You will also need to have a code editor(Visual studio is highly preferred)

## Execution


## Implementation

A database 'gamestore.db' is created when the create methods are first executed.

Customer Class/Table:
The Customer class represented the customers of the gaming store, encapsulating their name and email attributes. The customers table in the database stored these details with columns for id, name, and email. This class included methods for creating, reading, updating, and deleting customer records, ensuring data integrity through validations.

Game Class/Table:
The Game class modeled the games available in the store, including attributes for the game's name, price, and publisher. The games table in the database stored these details with columns for id, name, price, and publisher. This class provided methods for managing game records, incorporating validations to ensure that the game name was a non-empty string, the price was a non-negative number, and the publisher was a valid string.

Order Class/Table:
The Order class represented orders placed by customers, including attributes for the game ID, customer ID, and the date of the order. The orders table in the database included columns for id, game_ID, customer_ID, and date, with foreign keys ensuring referential integrity. This class included methods for managing order records, linking customers to the games they purchased and maintaining the order details.

OrderDetails Class/Table:
The OrderDetails class handled the specifics of each order, such as the quantity of each game ordered. The order_details table in the database stored these details with columns for id, OrderID, GameID, and quantity, with foreign keys linking the details to the respective orders and games. This class provided methods to manage order detail records, ensuring that the quantity was a positive integer and maintaining the relationships between orders and games.

--- From the main menu, the user is able to select an option of their liking. For the Option '0', the user able to select options which can allow them to:
        1. Check the full list of all the games available
        2. Add a new game to the database 
        3. Delete a game from the store
        4. Update a game
        5 Check the full list of all the games along with their orders

--- In the Option '1', a user can:
        1. View the full customer list
        2. Add a new customer
        3. Delete a customer
        4. Update a customer 
        5. View the customer orders
    in Option '2', a user can:
        1. View all the orders
        2. Add a new order
        3. Modify an order
        4. Delete an order
    in option '3', a user can:
        1. View all the order details
        2. Add a new order detail
        3. Delete an order detail
        4. Update an order detail
##   Conclusion
In conclusion, the development of the Game-Vault CLI application has successfully met several learning objectives. The implementation of a Command Line Interface in Python enabled the creation of a user-friendly interaction model through structured commands and clear prompts. Applying Object-Relational Mapping (ORM) techniques facilitated seamless integration between Python classes and SQLite databases, particularly in managing data persistence and retrieval across models like Customer, Game, Order, and OrderDetails. 

Establishing a one-to-many relationship between classes, such as Customers to Orders, underscored the importance of relational database principles and effective data modeling. This project helped improve technical skills and supported ideas like breaking down tasks into smaller parts, protecting data inside objects, and writing code that can be used again in different parts of the software.



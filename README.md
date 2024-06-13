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

Customer Class/Table:
The Customer class represented the customers of the gaming store, encapsulating their name and email attributes. The customers table in the database stored these details with columns for id, name, and email. This class included methods for creating, reading, updating, and deleting customer records, ensuring data integrity through validations.

Game Class/Table:
The Game class modeled the games available in the store, including attributes for the game's name, price, and publisher. The games table in the database stored these details with columns for id, name, price, and publisher. This class provided methods for managing game records, incorporating validations to ensure that the game name was a non-empty string, the price was a non-negative number, and the publisher was a valid string.

Order Class/Table:
The Order class represented orders placed by customers, including attributes for the game ID, customer ID, and the date of the order. The orders table in the database included columns for id, game_ID, customer_ID, and date, with foreign keys ensuring referential integrity. This class included methods for managing order records, linking customers to the games they purchased and maintaining the order details.

OrderDetails Class/Table:
The OrderDetails class handled the specifics of each order, such as the quantity of each game ordered. The order_details table in the database stored these details with columns for id, OrderID, GameID, and quantity, with foreign keys linking the details to the respective orders and games. This class provided methods to manage order detail records, ensuring that the quantity was a positive integer and maintaining the relationships between orders and games.

##   Conclusion
In conclusion, the development of the Game-Vault CLI application has successfully met several learning objectives. The implementation of a Command Line Interface in Python enabled the creation of a user-friendly interaction model through structured commands and clear prompts. Applying Object-Relational Mapping (ORM) techniques facilitated seamless integration between Python classes and SQLite databases, particularly in managing data persistence and retrieval across models like Customer, Game, Order, and OrderDetails. 

Establishing a one-to-many relationship between classes, such as Customers to Orders, underscored the importance of relational database principles and effective data modeling. This project helped improve technical skills and supported ideas like breaking down tasks into smaller parts, protecting data inside objects, and writing code that can be used again in different parts of the software.
















































```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   └── model_1.py
    ├── cli.py
    ├── debug.py
    └── helpers.py
```

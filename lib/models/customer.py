from models.__init__ import CURSOR, CONN
import re

class Customer:
    all = {}

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"Customer {self.id}: {self.name}, {self.email}"

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Enter a valid name")

    def get_email(self):
        return self._email

    def set_email(self, email):
        if self.validate_email(email):
            self._email = email
        else:
            raise ValueError(f"Invalid email address: {email}")

    name = property(get_name, set_name)
    email = property(get_email, set_email)

    @staticmethod
    def validate_email(email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new customer detail"""
        sql = """
            INSERT INTO customers (name, email)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.email))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, email):
        customer = cls(name, email)
        customer.save()
        return customer

    def update(self):
        sql = """
            UPDATE customers
            SET name = ?, email = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.email, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM customers
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM customers
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_email(cls, email):
        sql = """
            SELECT *
            FROM customers
            WHERE email = ?
        """
        row = CURSOR.execute(sql, (email,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM customers
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def instance_from_db(cls, row):
        if row:
            customer = cls(row[1], row[2])
            customer.id = row[0]
            cls.all[customer.id] = customer
            return customer
        return None

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM customers
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
  
    @classmethod
    def customer_orders(cls):
        sql = """
            SELECT customers.name, customers.email, games.name, OrderDetails.quantity
            FROM customers
            JOIN orders ON customers.id = orders.customer_ID
            JOIN OrderDetails ON orders.id = OrderDetails.OrderID
            JOIN games ON OrderDetails.GameID = games.id
        """
        rows = CURSOR.execute(sql).fetchall()
        for row in rows:
            print(f"Customer: {row[0]}, Email: {row[1]}, Game: {row[2]}, Quantity: {row[3]}")
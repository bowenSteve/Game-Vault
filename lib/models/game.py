from models.__init__ import CURSOR, CONN

class Game:
    all = {} 

    def __init__(self, name, price, publisher):
        self.name = name
        self.price = price
        self.publisher = publisher
    
    def __repr__(self):
        return f"Game {self.id}: Name: {self.name}, Price: {self.price}, Publisher: {self.publisher}"
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Enter a valid name")

    def get_price(self):
        return self._price
    
    def set_price(self, price):
        if isinstance(price, (int, float)) and price >= 0:
            self._price = price
            print(price)
        else:
            raise ValueError(f"Enter a valid price: {price}")

    def get_publisher(self):
        return self._publisher 
    
    def set_publisher(self, publisher):
        if isinstance(publisher, str) and len(publisher) > 0:
            self._publisher = publisher
        else:
            raise ValueError("Enter a valid publisher name")

    name = property(get_name, set_name)
    price = property(get_price, set_price)
    publisher = property(get_publisher, set_publisher)

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY,
            name TEXT,
            price REAL,
            publisher TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new game"""
        sql = """
            INSERT INTO games (name, price, publisher)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.price, self.publisher))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, price, publisher):
        game = cls(name, price, publisher)
        game.save()
        return game

    def update(self):
        sql = """
            UPDATE games
            SET name = ?, price = ?, publisher = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.price, self.publisher, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM games
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM games
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_publisher(cls, publisher):
        sql = """
            SELECT *
            FROM games
            WHERE publisher = ?
        """
        row = CURSOR.execute(sql, (publisher,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM games
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def instance_from_db(cls, row):
        game = cls(row[1], row[2], row[3])
        game.id = row[0]
        cls.all[game.id] = game
        return game

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM games
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
  
    @classmethod
    def games_with_orders(cls):
        sql = """
            SELECT g.id, g.name, g.price, g.publisher, o.id, o.date, od.Quantity
            FROM games g
            JOIN OrderDetails od ON g.id = od.GameID
            JOIN orders o ON o.id = od.OrderID
        """
        rows = CURSOR.execute(sql).fetchall()

        result = []
        for row in rows:
            game_order_info = {
                #"game_id": row[0],
                "Game name": row[1],
                "Game_price": row[2],
                "Game publisher": row[3],
               # "order_id": row[4],
                "Order date": row[5],
                "Order quantity": row[6]
            }
            result.append(game_order_info)

        return result


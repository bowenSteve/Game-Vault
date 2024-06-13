from models.__init__ import CURSOR, CONN

class Order_details:
    all = {}
    
    def __init__(self, order_id, game_id, quantity):
        self.order_id = order_id
        self.game_id = game_id
        self.quantity = quantity

    def __repr__(self):
        return f"ID {self.id}: Order ID: {self.order_id}, Game ID: {self.game_id} Quantity: {self.quantity}"

    def get_quantity(self):
        return self._quantity
    
    def set_quantity(self, quantity):
        if isinstance(quantity, int):
            self._quantity = quantity
        else:
            raise ValueError("Enter a valid quantity")
    
    quantity = property(get_quantity, set_quantity)

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS OrderDetails (
            id INTEGER PRIMARY KEY,
            OrderID INTEGER NOT NULL,
            GameID INTEGER NOT NULL,
            Quantity INTEGER NOT NULL,
            FOREIGN KEY (OrderID) REFERENCES Orders(id),
            FOREIGN KEY (GameID) REFERENCES Games(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new orderDetail"""
        sql = """
            INSERT INTO OrderDetails (OrderID, GameID, Quantity)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.order_id, self.game_id, self.quantity))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, order_id, game_id, quantity):
        orderDetail = cls(order_id, game_id, quantity)
        orderDetail.save()
        return orderDetail
    
    def update(self):
        sql = """
            UPDATE OrderDetails
            SET OrderID = ?, GameID = ?, Quantity = ?
            WHERE id = ?
            """
        CURSOR.execute(sql, (self.order_id, self.game_id, self.quantity, self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
            DELETE FROM OrderDetails
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM OrderDetails
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def instance_from_db(cls, row):
        order_detail = cls(row[1], row[2], row[3])
        order_detail.id = row[0]
        cls.all[order_detail.id] = order_detail
        return order_detail
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM OrderDetails
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

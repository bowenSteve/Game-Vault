from models.__init__ import CURSOR, CONN

class Order:
    all={}
    def __init__(self,game_ID,customer_ID, date):
        self.game_ID=game_ID
        self.customer_ID=customer_ID
        self.date=date

    def __repr__(self):
        return f"Orders {self.id}: {self.game_ID}, {self.customer_ID}, {self.date}"
    
    def get_date(self):
        return self._date
    def set_date(self, date):
        if isinstance(date, str):
            self._date=date
        else:
            raise ValueError("Enter a valid date")

    date=property(get_date, set_date)


    @classmethod
    def create_table(self):
        sql="""
            CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            game_ID INTEGER,
            customer_ID INTEGER,
            date TEXT, 
            FOREIGN KEY(game_ID) REFERENCES games(id),
            FOREIGN KEY(customer_ID) REFERENCES customers(id))
            """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new order"""
        sql = """
            INSERT INTO orders (game_ID, customer_ID, date)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.game_ID, self.customer_ID, self.date))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, game_ID, customer_ID, date):
        order = cls(game_ID, customer_ID, date)
        order.save()
        return order

    def update(self):
        sql = """
            UPDATE orders
            SET game_ID = ?, customer_ID = ?, date = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.game_ID, self.customer_ID, self.date, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM orders
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM orders
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_date(cls, date):
        sql = """
            SELECT *
            FROM orders
            WHERE date = ?
        """

        row = CURSOR.execute(sql, (date,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM orders
            WHERE id is ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    @classmethod
    def instance_from_db(cls, row):
        order = cls(row[1], row[2], row[3])
        order.id = row[0]
        cls.all[order.id] = order
        return order
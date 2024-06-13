from models.__init__ import CURSOR, CONN

class Publisher:
    all={}
    def __init__(self, name, country):
        self.name = name
        self.country = country
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError(f"The name {name} is invalid")

    def get_country(self):
        return self._country
    
    def set_country(self, country):
        if isinstance(country, str) and len(country) > 0:
            self._country = country
        else:
            raise ValueError(f"The country {country} is invalid")
    
    name = property(get_name, set_name)
    country = property(get_country, set_country)

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS publishers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            country TEXT )
            """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new publisher"""
        sql = """
            INSERT INTO publishers (name, country)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.country))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, country):
        publisher = cls(name, country)
        publisher.save()
        return publisher

    def update(self):
        sql = """
            UPDATE publishers
            SET name = ?, country = ?
            WHERE id = ?
            """
        CURSOR.execute(sql, (self.name, self.country, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM publishers
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM publishers
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_country(cls, country):
        sql = """
            SELECT *
            FROM publishers
            WHERE country = ?
        """

        row = CURSOR.execute(sql, (country,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM publishers
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

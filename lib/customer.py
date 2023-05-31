import sqlite3

CONN = sqlite3.connect('customer.db')
CURSOR = CONN.cursor()

class Customer:

    all = []

    def __init__(self, first_name, last_name):
        self.id = None
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT
            )
        """

        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS customers
        """

        CURSOR.execute(sql)

    @classmethod
    def new_from_db(cls, row):
        customer = cls(row[1], row[2])
        customer.id = row[0]
        return customer
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM customers
        """

        all = CURSOR.execute(sql).fetchall()
        
        cls.all = [cls.new_from_db(row) for row in all]

        return cls.all

    def save(self):
        sql = """
            INSERT INTO customers (first_name, last_name)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.first_name, self.last_name))

        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM customers").fetchone()[0]
        CONN.commit()

    @classmethod
    def create(cls, first_name, last_name):
        customer = Customer(first_name, last_name)
        customer.save()
        return customer
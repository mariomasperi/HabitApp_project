import sqlite3
"""
The class is used to manage the DB connection using context manager
"""

class DB_ContextManager:

    def __init__(self, db_name):
        """
        Constructor
        """
        self.db_name = db_name

    def __enter__(self):
        """
        Open the database connection
        """
        self.conn : sqlite3.Connection = sqlite3.connect(self.db_name)
        self.conn.execute("PRAGMA foreign_keys = ON")
        #self.cursor = sqlite3.Cursor = self.conn.cursor()

        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Close the connection
        """
        self.conn.close()
        if exc_val:
            raise
import logging
import sqlite3
from sqlite3 import Error

"""
This is the function-pool used to 
establish the database connection, create_connection method
and create the DB tables programmatically:
- habit_main
- habit_transaction
"""
SQL_CREATE_HABIT_TABLE = """ CREATE TABLE IF NOT EXISTS habit_main (    
                                        id integer PRIMARY KEY,      
                                        habit_name text NOT NULL,
                                        periodicity text NOT NULL,
                                        creation_date ANY,
                                        UNIQUE(habit_name)
                                    ); """

SQL_CREATE_HABIT_TR_TABLE = """ CREATE TABLE IF NOT EXISTS habit_transaction (
                                        id integer PRIMARY KEY,          
                                        habit_name text NOT NULL,
                                        periodicity text NOT NULL,
                                        completion_date ANY,
                                        habit_id integer,
                                        CONSTRAINT fk_habit
                                            FOREIGN KEY (habit_id) 
                                            REFERENCES habit_main(id) 
                                            ON DELETE CASCADE
                                    ); """
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.execute("PRAGMA foreign_keys = ON")
    except Error as e:
        print(e)

    return conn


def create_tables(conn):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(SQL_CREATE_HABIT_TABLE)
        c.execute(SQL_CREATE_HABIT_TR_TABLE)
    except Exception as Argument:
        logging.exception("Error in habit DB creation")
    else:
        return True


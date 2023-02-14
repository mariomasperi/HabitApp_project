import logging
# Habit table creation
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Exception as Argument:
        logging.exception("Error in habit DB creation")


#GLOBAL constant variables for tables creation
SQL_CREATE_HABIT_TABLE = """ CREATE TABLE IF NOT EXISTS habit_main (    
                                        id integer PRIMARY KEY,      
                                        habit_name text NOT NULL,
                                        periodicity text NOT NULL,
                                        creation_date ANY,
                                        UNIQUE(habit_name, periodicity)
                                    ); """

SQL_CREATE_HABIT_TR_TABLE = """ CREATE TABLE IF NOT EXISTS habit_transaction (
                                        id integer PRIMARY KEY,          
                                        habit_name text NOT NULL,
                                        periodicity text NOT NULL,
                                        completion_date ANY,
                                        habit_id integer NOT NULL,
                                        UNIQUE(habit_name, periodicity, habit_id),
                                        FOREIGN KEY (id) REFERENCES habit_main (id)
                                    ); """
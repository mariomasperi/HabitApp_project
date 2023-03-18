import logging
import analytics_function as analytics
"""
This is the Function-pool containing all functions
used to query in the Sqlite database tables
"""
# Get all records from Habit main table
def select_all(conn, query, param=None):
    """
    Select all records from the Habit Main menu
    """
    cur = conn.cursor()
    if param is not None:
        try:
            cur.execute(query, (param,))
        except Exception as e:
            print(e)
    else:
        try:
            cur.execute(query)
        except Exception as e:
            print(e)

    rows = cur.fetchall()


    return rows

def create_habit(conn, name, period, creation_date):
    """
    Create a new habit into the habit_main table
    :param conn:
    :param project:
    :return: project id
    """

    sql = ''' INSERT INTO habit_main(habit_name, periodicity , creation_date)
              VALUES(?,?,?) '''
    data_tuple = (name, period, creation_date)
    cur = conn.cursor()
    #cur = conn.cursor
    try:
        cur.execute(sql, data_tuple)
    except Exception as e:
        logging.exception("!!Error during Habit creation!!: " + str(e))

    conn.commit()

    return cur.lastrowid

def delete_habit(conn, name):
    """
    Delete Habit by name and period from DB (Habit_main and Habit_transaction)
    """
    GET_HABIT_BY_NAME = "SELECT * FROM habit_main WHERE habit_name = ?"
    DELETE_HABIT = "DELETE FROM habit_main where id = ?"

    cur = conn.cursor()
    #data_tuple = (name, period)
    try:
        cur.execute(GET_HABIT_BY_NAME, (name,))
    except Exception as e:
        logging.exception("Habit not found, error during query execution")
    else:
        rows = cur.fetchall()
        if not rows:
            logging.exception("Habit not found, error during query execution")
        else:
            habit_id = rows[0][0]
            try:
                cur.execute(DELETE_HABIT, (habit_id,))
            except Exception as e:
                print(e)
            else:
                #commit and show progress bar deletion
                conn.commit()
                return True



def update_habit_tr(conn, name, date):
    """
    Update habit_transaction table completion date
    """
    GET_HABIT_BY_NAME = "SELECT * FROM habit_main WHERE habit_name = ?"
    UPDATE_HABIT_TR = "INSERT INTO habit_transaction(habit_name, periodicity, completion_date, habit_id) VALUES (?,?,?,?)"
    cur = conn.cursor()
    #data_tuple = (name, period)
    try:
        cur.execute(GET_HABIT_BY_NAME, (name,))
    except Exception as e:
        print(e)
    else:
        rows = cur.fetchall()
        if not rows:
            logging.exception("Habit not found, error during query execution")
            habit = None
        else:
            data_update_tuple = (name, rows[0][2], date, rows[0][0])
            try:
                cur.execute(UPDATE_HABIT_TR, data_update_tuple)
            except Exception as e:
                print(e)
            else:
                conn.commit()

                habit = name

    return habit

"""
class ValueCache(object):
    def __init__(self, val=None):
        self.val = val
    def update(self, new):
        if self.val == new:
            return False
        else:
            self.val = new
            return True
"""










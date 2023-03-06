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
    try:
        cur.execute(sql, data_tuple)
    except Exception as e:
        logging.exception("!!Error during Habit creation!!: " + str(e))

    conn.commit()

    return cur.lastrowid

def delete_habit(conn, query1, query2, name):
    """
    Delete Habit by name and period from DB (Habit_main and Habit_transaction)
    """
    cur = conn.cursor()
    #data_tuple = (name, period)
    try:
        cur.execute(query1, (name,))
    except Exception as e:
        logging.exception("Habit not found, error during query execution")
    else:
        rows = cur.fetchall()
        if not rows:
            logging.exception("Habit not found, error during query execution")
        else:
            habit_id = rows[0][0]
            try:
                cur.execute(query2, (habit_id,))
            except Exception as e:
                print(e)
            else:
                #commit and show progress bar deletion
                conn.commit()
                analytics.progress_bar(name, "deleted")


def update_habit_tr(conn, query1, query2, name, date):
    """
    Update habit_transaction table completion date
    """
    cur = conn.cursor()
    #data_tuple = (name, period)
    try:
        cur.execute(query1, (name,))
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
                cur.execute(query2, data_update_tuple)
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










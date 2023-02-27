
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

def delete_habit(conn, query1, query2, name, period):
    """
    Delete Habit by name and period from DB (Habit_main and Habit_transaction)
    """
    cur = conn.cursor()
    data_tuple = (name, period)
    try:
        cur.execute(query1, data_tuple)
    except Exception as e:
        print(e)
    else:
        rows = cur.fetchall()
        habit_id = rows[0][0]
        try:
            cur.execute(query2, (habit_id,))
        except Exception as e:
            print(e)
        else:
            conn.commit()


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
        data_update_tuple = (name, rows[0][2], date, rows[0][0])
        try:
            cur.execute(query2, data_update_tuple)
        except Exception as e:
            print(e)
        else:
            conn.commit()

            habit = name

    return habit





class ValueCache(object):
    def __init__(self, val=None):
        self.val = val
    def update(self, new):
        if self.val == new:
            return False
        else:
            self.val = new
            return True











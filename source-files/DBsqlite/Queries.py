import Constant

# Get all records from Habit main table
def select_all(conn, query):
    """
    Select all records from the Habit Main menu
    """
    cur = conn.cursor()
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


def update_habit_tr(conn, query1, query2, name, period, date):
    """
    Update habit_transaction table completion date
    """
    cur = conn.cursor()
    data_tuple = (name, period)
    try:
        cur.execute(query1, data_tuple)
    except Exception as e:
        print(e)
    else:
        rows = cur.fetchall()
        data_update_tuple = (name, period, date, rows[0][0])
        try:
            cur.execute(query2, data_update_tuple)
        except Exception as e:
            print(e)
        else:
            conn.commit()
            #Set streak number
            #set_habit_streak(cur, rows[0][3],rows_tr[0][4], rows_tr[0][3], rows_tr[0][2],
            #                         rows_tr[0][5])

            habit = name

    return habit



def get_long_streak(conn, query):
    cur = conn.cursor()
    try:
        cur.execute(query)
    except Exception as e:
        print(e)
    else:
        rows = cur.fetchall()

    return rows













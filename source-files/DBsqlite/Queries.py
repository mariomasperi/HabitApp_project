import Constant
from datetime import datetime
import Habit
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

            habit = name

    return habit



def get_long_streak(conn, query):
    cur = conn.cursor()
    try:
        cur.execute(query)
    except Exception as e:
        print(e)
    else:
        habit_long_list = []
        rows = cur.fetchall()
        habit_dict = {}

        """
        Create dictionary for long streak calculation
        with HABIT NAME as key
        """
        for i, row in enumerate(rows):
            if row[0] in habit_dict:
                habit_dict[row[0]].append(row[1:])
            else:
                habit_dict[row[0]] = [row[1:]]
        #Calculate the long streak with the dictionary
        for key in habit_dict:
            values = habit_dict[key]
            streak = 0
            first = True
            for i, v in enumerate(values):
                if first:
                    creation_date = datetime.strptime(v[1], "%Y-%m-%d %H:%M:%S")
                    completion_date = datetime.strptime(v[2], "%Y-%m-%d %H:%M:%S")
                    update_date = completion_date
                    first = False
                else:
                    creation_date = datetime.strptime(values[i-1][2],"%Y-%m-%d %H:%M:%S")
                    completion_date = datetime.strptime(v[2], "%Y-%m-%d %H:%M:%S")


                count_day = completion_date - creation_date
                """
                if days passed from completion to creation date <= 1 for daily
                and <= 7 for weekly, we do have a streak for the habit
                """
                if v[0] == "D":
                    if count_day.days <= 1:
                        streak += 1
                if v[0] == "W":
                    if count_day.days <= 7:
                        streak += 1

                """
                if this is the last record add the streak and habit info
                to the habit object
                """
                if i == (len(values)-1):
                    streak_habit = Habit.Habit(key, creation_date, v[0])
                    streak_habit.add_streak(streak)
                    #append object to a list
                    habit_long_list.append(streak_habit)




















    return rows

class ValueCache(object):
    def __init__(self, val=None):
        self.val = val
    def update(self, new):
        if self.val == new:
            return False
        else:
            self.val = new
            return True











import Constant
from datetime import datetime, timedelta
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



def get_streak(conn, query):
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
                    previous_date = datetime.strptime(v[1], "%Y-%m-%d %H:%M:%S")
                    first = False
                    completion_date = datetime.strptime(v[2], "%Y-%m-%d %H:%M:%S")
                else:
                    previous_date = datetime.strptime(values[i - 1][2], "%Y-%m-%d %H:%M:%S")
                    completion_date = datetime.strptime(v[2], "%Y-%m-%d %H:%M:%S")
                    """
                    Check if the habit has been completed two times 
                    in the same day if DAILY frequency
                    and if it has been completed two time in the same week for WEEKLY frequency
                    """
                    if v[0] == "D":
                        if previous_date.day == completion_date.day:
                            continue
                    else:
                        week_number_prev = previous_date.isocalendar().week
                        week_number_comp = completion_date.isocalendar().week
                        if week_number_prev == week_number_comp:
                            continue


                #count_day = completion_date - previous_date
                if v[0] == "D":
                    num_days = 1
                else:
                    num_days = 7
                """
                if days passed from completion to creation date <= 1 for daily
                and <= 7 for weekly, we do have a streak for the habit
                """

                range_up_daily_completion = previous_date + timedelta(days=num_days)
                if previous_date <= completion_date <= range_up_daily_completion:
                    streak += 1
                else:
                    """
                    If streak is broke for the habit, exit from the loop
                    and save the streak count in the list
                    """
                    streak_habit = Habit.Habit(key, previous_date, v[0])
                    streak_habit.add_streak(streak)
                     # append object to a list
                    habit_long_list.append(streak_habit)
                    streak = 0

                """
                if this is the last record add the streak and habit info
                to the habit object
                """
                if i == (len(values)-1):
                    streak_habit = Habit.Habit(key, previous_date, v[0])
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











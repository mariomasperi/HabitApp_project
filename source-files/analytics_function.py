from datetime import datetime, timedelta
import Habit
import DBsqlite.Queries as q
from prettytable import PrettyTable
from rich.progress import track
import time


def get_streak(conn):
    """
    The queries extract the habits from the two tables executing a left join
    ordering the record from the oldest completion date
    """
    INNER_JOIN_HABIT = \
        "SELECT habit_transaction.habit_name, habit_transaction.periodicity, habit_main.creation_date, habit_transaction.completion_date FROM habit_transaction LEFT JOIN habit_main ON habit_transaction.habit_id = habit_main.id ORDER BY habit_transaction.habit_name, habit_transaction.periodicity, habit_transaction.completion_date;"
    cur = conn.cursor()
    try:
        cur.execute(INNER_JOIN_HABIT)
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
            for i, v in enumerate(values):
                #the code is taking the ifrst record as first date to be compared in the next
                #iterations
                if i == 0:
                    #previous_date = datetime.strptime(v[1], "%Y-%m-%d %H:%M:%S")
                    temp_previous_date = datetime.strptime(values[1][2], "%Y-%m-%d %H:%M:%S")
                else:
                    temp_previous_date = datetime.strptime(values[i - 1][2], "%Y-%m-%d %H:%M:%S")


                temp_completion_date = datetime.strptime(v[2], "%Y-%m-%d %H:%M:%S")
                """
                Check if the habit has been completed two times 
                in the same day if DAILY frequency
                and if it has been completed two time in the same week for WEEKLY frequency
                """
                if v[0] == "D":
                    if temp_previous_date.day == temp_completion_date.day:
                        continue
                    else:
                        previous_date   = temp_previous_date
                        completion_date = temp_completion_date
                        range_up_completion = previous_date + timedelta(days=1)
                else:
                    week_number_prev = temp_previous_date.isocalendar().week
                    week_number_comp = temp_completion_date.isocalendar().week
                    if week_number_prev == week_number_comp:
                        continue
                    else:
                        previous_date = week_number_prev
                        completion_date = week_number_comp
                        range_up_completion = week_number_prev + 1

                #range_up_daily_completion = previous_date + timedelta(days=num_days)
                if previous_date <= completion_date <= range_up_completion:
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

    return habit_long_list


def get_longest_streak(list_habits, param=None):
    #final_dict = {"habit": [], "streak": [], "periodicity": []}
    final_dict = {}
    support_list = []
    for i, habit in enumerate(list_habits):
        """
        if habit.name not in final_dict["habit"]:
            final_dict["habit"].append(habit.name)
            final_dict["streak"].append(habit._streak)
            final_dict["periodicity"].append(habit.periodicity)
        """
        #If enabled parameter habit name filter, select only the habit requested
        if param:
            if param == habit.name and param not in final_dict:
                final_dict[habit.name] = (habit.periodicity, habit._streak)
        else:
            if habit.name not in final_dict:
                final_dict[habit.name] = (habit.periodicity, habit._streak)

    return final_dict

def print_habit_analytics(items, param):
    t = PrettyTable(['Name', 'Period', param])
    for key, values in items.items():
        if values[0] == "W":
            period = "weekly"
        elif values[0] == "D":
            period = "daily"

        t.add_row([key, period, values[1]])

    return t

def display_habits(conn, period=None):
    """
    Get all habits items from habit_main table
    """
    if period:
        GET_HABITS = "SELECT * FROM habit_main WHERE periodicity = ?"
    else:
        GET_HABITS = "SELECT * FROM habit_main"

    items = q.select_all(conn, GET_HABITS, period)
    return items


def progress_bar(name, param):
    """
    Display a progress bar in the terminal
    """
    total = 0
    for value in track(range(100), description="Processing..."):
        # Fake processing time
        time.sleep(0.01)
        total += 1
    print("Habit {} {}!".format(name, param))
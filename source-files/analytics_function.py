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
    HISTORY_QUERY = "SELECT * FROM habit_transaction"

    cur = conn.cursor()
    try:
        # Execute the query left join habit_main and habit_transaction
        cur.execute(HISTORY_QUERY)
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
            if row[1] in habit_dict:
                habit_dict[row[1]].append(row[2:])
            else:
                habit_dict[row[1]] = [row[2:]]
        #Calculate the long streak with the dictionary
        for key in habit_dict:
            values = habit_dict[key]
            streak = 1
            for i, v in enumerate(values):
                # setup the completion date to compare with the next record
                temp_previous_date = datetime.strptime(values[i][1], "%Y-%m-%d %H:%M:%S")
                # set up the completion date of the next record
                temp_completion_date = datetime.strptime(values[i+1][1], "%Y-%m-%d %H:%M:%S")
                """
                Check if the habit has been completed two times in the same day if DAILY frequency
                and if it has been completed two time in the same week for WEEKLY frequency
                If not it the code is checking the following:
                - Daily: checking if the completion date happens in 24 hours range, if yes its a valid streak
                - Weekly: checking if the completion date happens during the next week range, if yes its a valid streak
                """
                if v[0] == "D":
                    if temp_previous_date.day == temp_completion_date.day and i != (len(values)-2):
                        continue
                    elif temp_previous_date.day == temp_completion_date.day and i == (len(values) - 2):
                        break
                    else:
                        previous_date   = temp_previous_date
                        completion_date = temp_completion_date
                        range_up_completion = previous_date + timedelta(days=1)
                else:
                    week_number_prev = temp_previous_date.isocalendar().week
                    week_number_comp = temp_completion_date.isocalendar().week
                    if week_number_prev == week_number_comp and i != (len(values)-2):
                        continue
                    elif week_number_prev == week_number_comp and i == (len(values)-2):
                        break
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
                    streak = 1

                """
                if this is the last record add the streak and habit info
                to the habit object
                """
                if i == (len(values)-2):
                    streak_habit = Habit.Habit(key, previous_date, v[0])
                    streak_habit.add_streak(streak)
                    #append object to a list
                    habit_long_list.append(streak_habit)
                    break


    return habit_long_list


def get_longest_streak(list_habits, param=None):
    """
    The function get the longest streak with enables filter parameter as habit name
    """
    final_dict = {}
    for i, habit in enumerate(list_habits):
        # If enabled parameter habit name filter, select only the habit requested
        # else select all habits
        if param:
            if param == habit.name and param not in final_dict:
                final_dict[habit.name] = (habit.periodicity, habit._streak)
        else:
            if habit.name not in final_dict:
                final_dict[habit.name] = (habit.periodicity, habit._streak)

    return final_dict

def print_habit_analytics(items, param):
    """
    Function to print the habit list in PrettyTable format
    """
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

def get_habit_byname(conn, name=None):
    """
    Get habits from habit_main table by habit name
    """
    GET_HABIT = "SELECT * FROM habit_main WHERE habit_name like ? ORDER BY habit_name DESC"

    items = q.select_all(conn, GET_HABIT, name)

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
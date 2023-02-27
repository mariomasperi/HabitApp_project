import Constant
import Habit
from datetime import date
import DBsqlite.DB_data_connection as db
import DBsqlite.create_new_habit_db as ct
import DBsqlite.DB_tables as db_create
from DBsqlite.DB_tables import SQL_CREATE_HABIT_TABLE
from DBsqlite.DB_tables import SQL_CREATE_HABIT_TR_TABLE
import DBsqlite.create_habit_tr_db as ct_tr
import Queries as q
import analytics_function as analytics
import datetime
from prettytable import PrettyTable
import operator

Constant.init()
conn = db.create_connection(Constant.database)

def create_habit():
    """
    Create a new Habit with NAME, PERIODICITY
    """
    # SQlite database address
    # connect to the database

    # Getting habit properties via user prompt
    habit_name = "GYM"
    periodicity = "W"
    while periodicity not in Constant.periodList:
        periodicity = "w"
    # Insert today as creation day
    creation_date = date.today()
    #Generate unique id
    habit = Habit.Habit(habit_name, creation_date, periodicity)
    #if connection to the DB is in place lets create a new record
    #in the Habit_main DB table
    if conn is not None:
        # create habit table
        db_create.create_table(conn, SQL_CREATE_HABIT_TABLE)
        # create Habt transaction table
        db_create.create_table(conn, SQL_CREATE_HABIT_TR_TABLE)

        habit_id = ct.create_habit(conn, habit)
        # create new record in habit transaction table
        if habit_id != 0:
            ct_tr.create_habit_tr(conn, habit, habit_id)

        print("this is the habit ID {}".format(habit_id))
    else:
        print("The connection is not established")

def display_all_habits():
    """
    Display all Habits list
    """
    items = q.select_all(conn, Constant.GET_ALL_HABITS)
    t = PrettyTable(['Name', 'Period'])
    for i in items:
        if i[2] == "W":
            period = "weekly"
        elif i[2] == "D":
            period = "daily"

        t.add_row([i[1], period])

    print(t)

def delete_habit():
    """
    Delete an existing Habit by NAME and PERIOD
    """
    # Getting habit properties via user prompt
    habit_name = "TEST"
    periodicity = "D"

    q.delete_habit(conn, Constant.GET_HABIT_BY_NAME_PERIO, Constant.DELETE_HABIT, habit_name, periodicity)
    print("deleting habit")

def mark_habit_completed():
    """
    Delete an existing Habit by NAME and PERIOD
    """
    # Getting habit properties via user prompt
    habit_name = "RUN"
    periodicity = "D"

    completed_date = datetime.datetime.now()

    q.update_habit_tr(conn, Constant.GET_HABIT_BY_NAME_PERIO, Constant.UPDATE_HABIT_TR, habit_name, periodicity,
                      completed_date)


def longest_streak():
    items = analytics.get_streak(conn, Constant.INNER_JOIN_HABIT)
    #Sort Habit object list by name and streak DESC
    items_sort = sorted(items, key = lambda x: (x.name, -x._streak))
    #Get only the longest streak by habit
    final_list = analytics.get_longest_streak(items_sort)
    # Print habit list
    table = analytics.print_habit_analytics(final_list, Constant.long_streak)

    print(table)

def get_all_habits_byPerio():
    """
    Display all habits list by period, choose daily("D") or weekly("W")
    """
    periodicity = "D"
    #Display habits list by period selected
    items = analytics.display_habits(conn, Constant.GET_HABITS_BY_PERIO, periodicity)
    t = PrettyTable(['Name', 'Period', 'Creation date'])
    for i in items:
        if i[2] == "W":
            period = "weekly"
        elif i[2] == "D":
            period = "daily"

        t.add_row([i[1], period, i[3]])

    print(t)

def longest_habit_streak_byHabit():
    """
    Display the longest run streak for a given Habit
    Please insert the Habit name
    """
    habit_name = "RUN"
    #Get all list of habits streak
    habits_streak_list = analytics.get_streak(conn, Constant.INNER_JOIN_HABIT)
    #Sort Habit object list by name and streak DESC
    items_sort = sorted(habits_streak_list, key = lambda x: (x.name, -x._streak))
    #Get long streak by Habit
    habit = analytics.get_longest_streak(items_sort, habit_name)
    #Print habit list
    table = analytics.print_habit_analytics(habit, Constant.long_streak)

    print(table)

if __name__ == '__main__':
    #create_habit()
    #display_all_habits()
    #delete_habit()
    #mark_habit_completed()
    #longest_streak()
    #get_all_habits_byPerio()
    longest_habit_streak_byHabit()
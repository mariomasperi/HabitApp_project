import typer
from prettytable import PrettyTable
import DBsqlite.DB_tables as db_create
from DBsqlite.DB_tables import SQL_CREATE_HABIT_TABLE
from DBsqlite.DB_tables import SQL_CREATE_HABIT_TR_TABLE
import analytics_function as analytics
from context_manager import DB_ContextManager

"""
This is the Analytics menu, containing the following commands:

1. display_all_habits - to display all habits list in the terminal
2. longest_habit_streak - to display the longest habits streak list in the terminal
3. get_all_habits_byPerio - to display the habits list filtered by periodicity in the terminal
4. longest_habit_streak_byHabit - to display the longest streak filtered by Habit in the terminal
"""

analytics_menu = typer.Typer()
#Establish connection to database if not done yet
#database = "/Users/u1127499/Desktop/HabitApp_project/identifier.sqlite"

database = "habits.db"

with DB_ContextManager(database) as conn:
    if conn is not None:
        bool = db_create.create_tables(conn)

@analytics_menu.command()
def display_all_habits():
    """
    Display all Habits list
    """
    #Get all habits list
    with DB_ContextManager(database) as conn:
        if conn is not None:
            items = analytics.display_habits(conn)
            if items:
                #display habits information
                t = PrettyTable(['Name', 'Period', 'Creation date'])
                for i in items:
                    if i[2] == "W":
                        period = "weekly"
                    elif i[2] == "D":
                        period = "daily"

                    t.add_row([i[1], period, i[3]])

                print(t)
            else:
                print ("No habits found")

@analytics_menu.command()
def longest_habit_streak():
    """
    Return the longest number of streaks for all habits
    """
    #Get all list of habits streak
    with DB_ContextManager(database) as conn:
        if conn is not None:
            habits_streak_list = analytics.get_streak(conn)
            if habits_streak_list:
                #Sort Habit object list by name and streak DESC
                items_sort = sorted(habits_streak_list, key = lambda x: (x.name, -x._streak))
                #Get long streaks in habits list
                habit = analytics.get_longest_streak(items_sort)
                #Print habit list
                long_streak = "Longest number of streak"
                table = analytics.print_habit_analytics(habit, long_streak)

                print(table)
            else:
                print("No habits found")


@analytics_menu.command()
def get_all_habits_byPerio():
    """
    Display all habits list by period, choose daily("D") or weekly("W")
    """
    #Get periodicity from user input (choose daily or weekly)
    periodicity = str.upper(typer.prompt("Please enter the periodicity w/d, use W for weekly and D for daily"))
    periodList = ["W", "D"]
    while periodicity not in periodList:
        periodicity = str.upper(typer.prompt("Please use W for weekly and D for daily, not others value are allowed"))
    #Display habits list by period selected
    with DB_ContextManager(database) as conn:
        if conn is not None:
            items = analytics.display_habits(conn, periodicity)
            if items:
                # display habits information
                t = PrettyTable(['Name', 'Period', 'Creation date'])
                for i in items:
                    if i[2] == "W":
                        period = "weekly"
                    elif i[2] == "D":
                        period = "daily"

                    t.add_row([i[1], period, i[3]])

                print(t)
            else:
                print ("No habits found")

@analytics_menu.command()
def longest_habit_streak_byHabit():
    """
    Display the longest run streak for a given Habit
    Please insert the Habit name
    """
    habit_name = str.upper(typer.prompt("Please enter the habit name"))
    #Get all list of habits streak
    with DB_ContextManager(database) as conn:
        if conn is not None:
            habits_streak_list = analytics.get_streak(conn)
            if habits_streak_list:
                #Sort Habit object list by name and streak DESC
                items_sort = sorted(habits_streak_list, key = lambda x: (x.name, -x._streak))
                #Get long streak by Habit
                habit = analytics.get_longest_streak(items_sort, habit_name)
                #Print habit list
                long_streak = "Longest number of streak"
                table = analytics.print_habit_analytics(habit, long_streak)

                print(table)
            else:
                print("No habits found")



if __name__ == "__main__":
    analytics_menu()
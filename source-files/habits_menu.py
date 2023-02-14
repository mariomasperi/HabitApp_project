import typer
import Habit
from datetime import date
import DBsqlite.DB_data_connection as db
import DBsqlite.create_new_habit_db as ct
import Constant
import DBsqlite.DB_tables as db_create
from DBsqlite.DB_tables import SQL_CREATE_HABIT_TABLE
from DBsqlite.DB_tables import SQL_CREATE_HABIT_TR_TABLE
import DBsqlite.create_habit_tr_db as ct_tr
import Queries as q
from prettytable import PrettyTable

habits_menu = typer.Typer()
#Init global variables
Constant.init()
conn = db.create_connection(Constant.database)


@habits_menu.command()
def create_habit():
    """
    Create a new Habit with NAME, PERIODICITY
    """
    # Getting habit properties via user prompt
    habit_name = str.upper(typer.prompt("Please enter the habit name"))
    periodicity = str.upper(typer.prompt("Please enter the periodicity w/d, use W for weekly and D for daily"))
    while periodicity not in Constant.periodList:
        periodicity = str.upper(typer.prompt("Please use W for weekly and D for daily, not others value are allowed"))

    # Insert today as creation day
    creation_date = date.today()
    # create new Habit object
    habit = Habit.Habit(habit_name, creation_date, periodicity)
    #if connection to the DB is in place lets create a new record
    #in the Habit_main DB table
    if conn is not None:
        # create habit table
        db_create.create_table(conn, SQL_CREATE_HABIT_TABLE)
        # create Habt transaction table
        db_create.create_table(conn, SQL_CREATE_HABIT_TR_TABLE)
        # create habit on DB
        habit_id = ct.create_habit(conn, habit)
        # create new record in habit transaction table
        if habit_id != 0:
            ct_tr.create_habit_tr(conn, habit, habit_id)
            ct.progress_bar(habit_name)
        else:
            print("error on Habit creation")

@habits_menu.command()
def delete_habit(name: str):
    """
    Delete an existing Habit by NAME
    """

    print("deleting habit")


@habits_menu.command()
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


    #print("display all habits list")


@habits_menu.command()
def display_habit_byName(name: str):
    """
    Display Habit by NAME
    """
    print("display habit")


@habits_menu.command()
def display_habit_byPeriodicity(periodicity: str):
    """
    Display Habit by PERIOD
    """
    print("display habit by period")


@habits_menu.command()
def mark_habit_completed(habit: str):
    """
    Mark an habit as completed
    """
    print("display habit by period")


if __name__ == "__main__":
    habits_menu()

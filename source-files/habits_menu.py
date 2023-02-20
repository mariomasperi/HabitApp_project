import typer
import Habit
import datetime
from prettytable import PrettyTable
import DBsqlite.DB_data_connection as db
import DBsqlite.create_new_habit_db as ct
import Constant
import DBsqlite.DB_tables as db_create
from DBsqlite.DB_tables import SQL_CREATE_HABIT_TABLE
from DBsqlite.DB_tables import SQL_CREATE_HABIT_TR_TABLE
import DBsqlite.create_habit_tr_db as ct_tr
import DBsqlite.Queries as q


habits_menu = typer.Typer()
# Init global variables
Constant.init()
conn = db.create_connection(Constant.database)
if conn is not None:
    # create habit table
    db_create.create_table(conn, SQL_CREATE_HABIT_TABLE)
    # create Habit transaction table
    db_create.create_table(conn, SQL_CREATE_HABIT_TR_TABLE)

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
    creation_date = datetime.datetime.now()
    # create new Habit object
    habit = Habit.Habit(habit_name, creation_date, periodicity)
    # if connection to the DB is in place lets create a new record
    # in the Habit_main DB table
    if conn is not None:
        # create habit on DB
        habit_id = ct.create_habit(conn, habit)
        # create new record in habit transaction table
        if habit_id:
            ct_tr.create_habit_tr(conn, habit, habit_id)
            ct.progress_bar(habit_name, "created")
        else:
            print("error on Habit creation")


@habits_menu.command()
def delete_habit():
    """
    Delete an existing Habit by NAME and PERIOD
    """
    # Getting habit properties via user prompt
    habit_name = str.upper(typer.prompt("Please enter the habit name you want to delete"))
    periodicity = str.upper(typer.prompt("Please enter the habit periodicity w/d, use W for weekly and D for daily"))
    while periodicity not in Constant.periodList:
        periodicity = str.upper(typer.prompt("Please use W for weekly and D for daily, not others value are allowed"))

    q.delete_habit(conn, Constant.GET_HABIT_BY_NAME_PERIO, Constant.DELETE_HABIT, habit_name, periodicity)
    print("deleting habit")



@habits_menu.command()
def mark_habit_completed():
    """
    Mark habit as completed
    """
    # Getting habit properties via user prompt
    habit_name = str.upper(typer.prompt("Please enter the habit name you want to mark as completed"))
    periodicity = str.upper(typer.prompt("Please enter the habit periodicity w/d, use W for weekly and D for daily"))
    while periodicity not in Constant.periodList:
        periodicity = str.upper(typer.prompt("Please use W for weekly and D for daily, not others value are allowed"))

    flag = str.upper(typer.prompt("Are you sure you want to complete the habit (y/n)"))
    if flag == "Y":
        completed_date = datetime.datetime.now()
        habit = q.update_habit_tr(conn, Constant.GET_HABIT_BY_NAME_PERIO, Constant.UPDATE_HABIT_TR,
                          habit_name, periodicity, completed_date)
        if habit:
            ct.progress_bar(habit, "completed")
        else:
            print("error on Habit completion")






if __name__ == "__main__":
    habits_menu()

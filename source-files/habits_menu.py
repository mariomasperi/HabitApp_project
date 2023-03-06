import typer
import datetime
import Constant
import DBsqlite.DB_tables as db_create
from DBsqlite.DB_tables import SQL_CREATE_HABIT_TABLE
from DBsqlite.DB_tables import SQL_CREATE_HABIT_TR_TABLE
import DBsqlite.Queries as q
import analytics_function as analytics

"""
This is the Habit menu, containing the following commands:

1. create_habit - to create a new habit
2. delete_habit - to delete an existing habit
3. mark_habit_completed - to mark an habit as completed
"""

habits_menu = typer.Typer()
# Init global variables
Constant.init()
conn = db_create.create_connection(Constant.database)
#Establish connection to database if not done yet
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
    creation_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # if connection to the DB is in place lets create a new record
    # in the Habit_main DB table
    if conn is not None:
        # create habit on DB
        habit_id = q.create_habit(conn, habit_name, periodicity, creation_date )
        # show progress bar if Habit is successfully created
        if habit_id:
            analytics.progress_bar(habit_name, "created")
        else:
            print("error on Habit creation")


@habits_menu.command()
def delete_habit():
    """
    Delete an existing Habit by NAME
    """
    # Getting habit properties via user prompt
    habit_name = str.upper(typer.prompt("Please enter the habit name you want to delete"))
    """
    periodicity = str.upper(typer.prompt("Please enter the habit periodicity w/d, use W for weekly and D for daily"))
    while periodicity not in Constant.periodList:
        periodicity = str.upper(typer.prompt("Please use W for weekly and D for daily, not others value are allowed"))
    """
    q.delete_habit(conn, Constant.GET_HABIT_BY_NAME, Constant.DELETE_HABIT, habit_name)
    print("deleting habit")



@habits_menu.command()
def mark_habit_completed():
    """
    Mark habit as completed
    """
    # Getting habit properties via user prompt
    habit_name = str.upper(typer.prompt("Please enter the habit name you want to mark as completed"))
    #periodicity = str.upper(typer.prompt("Please enter the habit periodicity w/d, use W for weekly and D for daily"))
    #while periodicity not in Constant.periodList:
    #    periodicity = str.upper(typer.prompt("Please use W for weekly and D for daily, not others value are allowed"))
    #Ask confirmation to the user about completing an habit
    flag = str.upper(typer.prompt("Are you sure you want to complete the habit (y/n)"))
    if flag == "Y":
        #taking complete date information
        completed_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #create habit in transactional table
        habit = q.update_habit_tr(conn, Constant.GET_HABIT_BY_NAME, Constant.UPDATE_HABIT_TR,
                          habit_name, completed_date)
        #if habit is created shows a progress bar otherwise printout an error
        if habit:
            analytics.progress_bar(habit, "completed")
        else:
            print("error on Habit completion")



if __name__ == "__main__":
    habits_menu()

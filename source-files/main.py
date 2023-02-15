import typer
import habits_menu
import analytics_menu
import Constant
import DBsqlite.DB_tables as db_create
import DBsqlite.DB_data_connection as db
from DBsqlite.DB_tables import SQL_CREATE_HABIT_TABLE
from DBsqlite.DB_tables import SQL_CREATE_HABIT_TR_TABLE

app = typer.Typer()
# Initialize the global variables
# Init global variables
Constant.init()
conn = db.create_connection(Constant.database)
if conn is not None:
    # create habit table
    db_create.create_table(conn, SQL_CREATE_HABIT_TABLE)
    # create Habit transaction table
    db_create.create_table(conn, SQL_CREATE_HABIT_TR_TABLE)

app.add_typer(habits_menu.habits_menu, name="habit", help="Habit management menu")
app.add_typer(analytics_menu.analytics_menu, name="analytics", help="Analytics module")

if __name__ == '__main__':
    app()

"""
@click.group()
def menu():

    pass

@menu.group(chain = True)
def habits():
    pass

@menu.group(chain = True)
def profile():
    pass

@click.command()
def get_profile():
    print("get profile list")

@click.command()
def create_habits():

    habit_name = typer.prompt("Please type the habit's name")
    print("Hello" + {habit_name})

habits.add_command(create_habits)
profile.add_command(get_profile)
"""

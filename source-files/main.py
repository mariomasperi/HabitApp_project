import typer
import habits_menu
import Constant

app = typer.Typer()
# Initialize the global variables
#Constant.init()
app.add_typer(habits_menu.habits_menu, name="habit", help="Habit menu please use --help")

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

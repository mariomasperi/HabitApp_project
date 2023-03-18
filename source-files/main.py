import typer
import habits_menu
import analytics_menu

# Invoke the typer class
app = typer.Typer()
# Initialize the application main menu: habit and analytics
app.add_typer(habits_menu.habits_menu, name="habit", help="Habits menu")
app.add_typer(analytics_menu.analytics_menu, name="analytics", help="Analytics menu")

if __name__ == '__main__':
    app()


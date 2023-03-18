import analytics_function
from context_manager import DB_ContextManager
import DBsqlite.DB_tables as db_create
import DBsqlite.Queries as q
import analytics_function as analytics

database = "habits.db"

def test_longest_habit_streak():
    """
    Get longest streak habit list
    """
    #Get all list of habits streak
    with DB_ContextManager(database) as conn:
        if conn is not None:
            habits_streak_list = analytics.get_streak(conn)
            if habits_streak_list:
                #Sort Habit object list by name and streak DESC
                items_sort = sorted(habits_streak_list, key = lambda x: (x.name, -x._streak))
                #Get long streaks in habits list
                habit_list = analytics.get_longest_streak(items_sort)

                assert len(habit_list) != 0, "habit list is empty, no streak found"
            else:
                assert 1 == 2, "habit list is empty, no streak found"
        else:
            assert 1 == 2, "connection to DB not established"

def test_get_habits_byperiod():
    """
    Get habits by periodicity test
    """
    with DB_ContextManager(database) as conn:
        if conn is not None:
            periodicity = "W"
            items = analytics.display_habits(conn, periodicity)
            assert len(items) != 0, "No habits found"
        else:
            assert 1 == 2, "connection to DB not established"

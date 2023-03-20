from context_manager import DB_ContextManager
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
            # Check if any habits exist for habit period as weekly
            periodicity = "W"
            items = analytics.display_habits(conn, periodicity)
            if items:
                assert len(items) != 0, "No habits found for weekly period"
            else:
                # Check if any habits exist for habit period as daily
                periodicity = "D"
                items_d = analytics.display_habits(conn, periodicity)
                assert len(items_d) != 0, "No habits found for daily period"
        else:
            assert 1 == 2, "connection to DB not established"

def test_display_all_habits():
    """
    Display all habits function test
    """
    with DB_ContextManager(database) as conn:
        if conn is not None:
            items = analytics.display_habits(conn)
            assert len(items) != 0, "No habits found"
        else:
            assert 1 == 2, "connection to DB not established"

def test_longest_habit_streak_byhabit():
    """
    Get the longest streak filtered by habit test function
    """
    with DB_ContextManager(database) as conn:
        if conn is not None:
            habits_streak_list = analytics.get_streak(conn)
            if habits_streak_list:
                first_object = habits_streak_list[0]
                #Sort Habit object list by name and streak DESC
                items_sort = sorted(habits_streak_list, key = lambda x: (x.name, -x._streak))
                #Get long streak by Habit
                habit = analytics.get_longest_streak(items_sort, first_object.name )
                assert len(habit) !=0, "No habits found"
            else:
                assert 1 == 2, "No habits with streak found"
        else:
            assert 1 == 2, "connection to DB not established"

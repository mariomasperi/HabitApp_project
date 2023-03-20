import Habit
import datetime
import analytics_function
from context_manager import DB_ContextManager
import DBsqlite.DB_tables as db_create
import DBsqlite.Queries as q
import analytics_function as analytics

database = "habits.db"

def test_create_db():
    """
    test db connection and tables creation
    """
    with DB_ContextManager(database) as conn:
        if conn is not None:
            check = db_create.create_tables(conn)
            assert check == True, "tables creation failed"
        else:
            assert 1 == 2, "connection to DB not established"



def test_habit_creation():
    """
    test habit creation function
    """
    creation_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_habit = Habit.Habit("TEST_CREATION_%", creation_date, "W")
    with DB_ContextManager(database) as conn:
        if conn is not None:
            items = analytics.get_habit_byname(conn, new_habit.name)
            if items:
                """
                if the habit exist create a new TEST habit adding 1 to the counter
                """
                name_len = len(items[0][1])
                slice_counter = int(items[0][1][name_len-1:name_len]) + 1
                habit_prefix = "TEST_CREATION_"
                new_habit_name = habit_prefix + str(slice_counter)
                new_habit.name = new_habit_name

                habit_id = q.create_habit(conn, new_habit.name, new_habit.periodicity,
                                          new_habit.creation_date)
            else:
                """
                if habit test doesnt exist create a new one
                """
                new_habit.name = "TEST_CREATION_1"
                habit_id = q.create_habit(conn, new_habit.name, new_habit.periodicity,
                                          new_habit.creation_date)

            assert habit_id != 0, "habit creation failed"

        else:
            assert 1 == 2, "connection to DB not established"


def test_habit_deletion():
    """
    Delete one habit from database
    """
    with DB_ContextManager(database) as conn:
        if conn is not None:
            habit_list = analytics_function.display_habits(conn)
            if habit_list:
                name = habit_list[0][1]
                assert q.delete_habit(conn, name) == True, "Deletion failed"
            else:
                assert 1 == 2, "no habits found"
        else:
            assert 1 == 2, "connection to DB not established"

def test_mark_habit_completed():
    """
    Mark an habit as completed
    """
    with DB_ContextManager(database) as conn:
        if conn is not None:
            habit_list = analytics_function.display_habits(conn)
            if habit_list:
                name = habit_list[0][1]
                completed_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                habit = q.update_habit_tr(conn, name, completed_date)

                assert len(habit) != 0, "habit failed to be marked as completed"
            else:
                assert 1 == 2, "no habits found"
        else:
            assert 1 == 2, "connection to DB not established"


















"""
This python script contains all global variables used by the application:
1. Database location
2. analytics constant
3. SQL queries
"""



def init():
    """
    Initialization of global variables
    """
    global database, periodList, long_streak, GET_ALL_HABITS, \
        GET_HABIT_BY_NAME, DELETE_HABIT, UPDATE_HABIT_TR, GET_HABIT_TR_BY_ID, UPDATE_HABIT_TR_STREAK, \
        INNER_JOIN_HABIT, GET_HABITS_BY_PERIO

    database = "/Users/u1127499/Desktop/HabitApp_project/identifier.sqlite"
    periodList = ["W", "D"]
    long_streak = "Longest number of streak"
    """
    QUERY variables list
    """
    GET_ALL_HABITS = "SELECT * FROM habit_main"
    GET_HABIT_BY_NAME = "SELECT * FROM habit_main WHERE habit_name = ?"
    GET_HABITS_BY_PERIO = "SELECT * FROM habit_main WHERE periodicity = ?"
    DELETE_HABIT = "DELETE FROM habit_main where id = ?"
    #UPDATE_HABIT_TR = "UPDATE habit_transaction SET completion_date = ? WHERE habit_id = ?"
    UPDATE_HABIT_TR = "INSERT INTO habit_transaction(habit_name, periodicity, completion_date, habit_id) VALUES (?,?,?,?)"
    UPDATE_HABIT_TR_STREAK = "UPDATE habit_transaction SET streak = ? WHERE habit_id = ?"
    GET_HABIT_TR_BY_ID = "SELECT * FROM habit_transaction where habit_id = ?"
    INNER_JOIN_HABIT = \
        "SELECT habit_transaction.habit_name, habit_transaction.periodicity, habit_main.creation_date, habit_transaction.completion_date FROM habit_transaction LEFT JOIN habit_main ON habit_transaction.habit_id = habit_main.id ORDER BY habit_transaction.habit_name, habit_transaction.periodicity, habit_transaction.completion_date;"


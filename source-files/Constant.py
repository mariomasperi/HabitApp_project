

def init():
    global database, periodList, GET_ALL_HABITS, GET_HABIT_BY_NAME_PERIO, DELETE_HABIT
    database = "/Users/u1127499/Desktop/HabitApp_project/identifier.sqlite"
    periodList = ["W", "D"]
    #QUERIES
    GET_ALL_HABITS = "SELECT * FROM habit_main"
    GET_HABIT_BY_NAME_PERIO = "SELECT * FROM habit_main WHERE habit_name = ? and periodicity = ?"
    DELETE_HABIT = "DELETE FROM habit_main where id = ?"


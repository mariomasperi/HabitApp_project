

def init():
    global database, periodList, GET_ALL_HABITS
    database = "/Users/u1127499/Desktop/HabitApp_project/identifier.sqlite"
    periodList = ["W", "D"]
    #QUERIES
    GET_ALL_HABITS = "SELECT * FROM habit_main"


"""
This is the Habit class
1. The Habit class create an object with the following attributes:
-id: int
-name:string
-creation_date: datetime
-periodicity: string
-completion_date: datetime
-num_streak: int

2. The Habit class contain the following methods:
+delete(name)
+get_habit_by_name(name)
+set_habit_completed(name, completion_date)
"""


class Habit:
    #Constructor
    def __init__(self, name, creation_date, periodicity):
        #Instance variable
        self.name = name
        self.creation_date = creation_date
        self.periodicty = periodicity






"""
This is the Habit class
1. The Habit class create an object with the following attributes:
-name:string
-creation_date: datetime
-periodicity: string
-completion_date: datetime
-_streak: int
-_completion_date: datetime

2. The Habit class contain the following methods:
+add_streak(self, streak)
+set_completion_date(self, date)
"""


class Habit:
    #Constructor
    def __init__(self, name, creation_date, periodicity):
        #Instance variable
        self._completion_date = None
        self._streak = 0
        self.name = name
        self.creation_date = creation_date
        self.periodicity = periodicity

    def add_streak(self, streak):
        self._streak = streak
    
    def set_completion_date(self, date):
        self._completion_date = date






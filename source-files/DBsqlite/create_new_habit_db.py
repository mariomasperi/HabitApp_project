import sqlite3
import Habit
from sqlite3 import Error
import logging
from rich.progress import track
import time


def create_habit(conn, habit):
    """
    Create a new habit into the habit_main table
    :param conn:
    :param project:
    :return: project id
    """

    sql = ''' INSERT INTO habit_main(habit_name, periodicity , creation_date)
              VALUES(?,?,?) '''
    data_tuple = (habit.name, habit.periodicty, habit.creation_date)
    cur = conn.cursor()
    try:
        cur.execute(sql, data_tuple)
    except Exception as e:
        logging.exception("!!Error during Habit creation!!: " + str(e))

    conn.commit()

    return cur.lastrowid

#progress habit created
def progress_bar(name, param):
    total = 0
    for value in track(range(100), description="Processing..."):
        # Fake processing time
        time.sleep(0.01)
        total += 1
    print("Habit {} {}!".format(name, param))

def create_transaction(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO habit_transaction(habit_name, habit_periodicity, completion_date)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid

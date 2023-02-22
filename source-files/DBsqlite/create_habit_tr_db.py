import sqlite3
import Habit
from sqlite3 import Error
import logging


def create_habit_tr(conn, query1, habit, period):
    """
    Create a new habit into the habit_main table
    :param conn:
    :param project:
    :return: project id
    """
    cur = conn.cursor()
    data_tuple = (habit, period)
    try:
        cur.execute(query1, data_tuple)
    except Exception as e:
        print(e)
    else:
        sql = ''' INSERT INTO habit_transaction(habit_name, periodicity , habit_id)
                  VALUES(?,?,?) '''
        data_tuple = (habit.name, habit.periodicty, id)
        cur = conn.cursor()
        try:
            cur.execute(sql, data_tuple)
        except Exception as e:
            logging.exception("!!Error during Habit creation!!: " + str(e))

        conn.commit()

    return cur.lastrowid


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

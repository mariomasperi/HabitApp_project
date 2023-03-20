# Habit application project

The project scope is building an application to create and mainatin daily and weekly habits, its uses Python 3.11

# Installation

The project use externaly libraries to function:
1. **Typer** CLI library - https://typer.tiangolo.com/
  This is a library for building CLI applications based on Python , use pip command to install from the terminal:
  
  *pip install "typer[all]"*
  
  ![image](https://user-images.githubusercontent.com/10673190/226419353-9463773a-8d30-44c1-8c07-98456dd67d0c.png)

2. **PrettyTable** library - https://pypi.org/project/prettytable/
  This library used to print tables in attractive ASCII form, use pip command to install from the terminal:

  *python -m pip install -U prettytable*
  
3. **Rich** library - https://pypi.org/project/rich/
  This library is used to create beautiful formatting in the terminal, use pip command to install from the terminal:
  
  *python -m pip install rich*
  
  
# How to Use?

The application must be executed from the terminal. 
The menu is launched, using the following command:
*python main.py --help*

To access to the habit menu instead use the following, just adding the *habit*  word after *main*:
*python main.py habit --help*

To access to the analytics menu instead use the following, just adding the *analytics*  word after *main*:
*python main.py analytics --help*

Here a short video that shows how it works:

https://user-images.githubusercontent.com/10673190/226424977-b6113acb-bb70-4767-b4fe-871edd96bd8a.mov

**In the HABIT MENU you can trigger the following commands to:**
1. *python main.py habit create-habit*

  To create a new habit, just insert the name and the frequency

  ![image](https://user-images.githubusercontent.com/10673190/226425654-f31183fb-ee34-414a-887f-25d617e69cd2.png)

2. *python main.py habit mark-habit-completed*

  To mark an habit as completed, just insert the name of the habit and confirm the operation:
  
  ![image](https://user-images.githubusercontent.com/10673190/226426090-9b60fae0-c870-4c06-bda8-6ea267cc254f.png)

3. *python main.py habit delete-habit*

  To delete an existing habit, enter the habit name:
  
  ![image](https://user-images.githubusercontent.com/10673190/226426404-52c67194-6f6c-4f8c-9715-08412c0a4690.png)


**In the ANALYTICS MENU you can trigger the following commands to:**

1. *python main.py analytics display-all-habits*

  To display all habits in the database:

  ![image](https://user-images.githubusercontent.com/10673190/226426912-c8ce3628-5b4b-4091-9131-2169f51d51cd.png)

2. *python main.py analytics get-all-habits-byperio*

  To display all habits filter by periodicity, enter daily(d) or weekly (w):
  
  ![image](https://user-images.githubusercontent.com/10673190/226427180-2c33b373-abaa-45df-99c2-3a28c60c857d.png)

3. *python main.py analytics longest-habit-streak*

  To display all habits longest streak:
  
  ![image](https://user-images.githubusercontent.com/10673190/226427475-8da59eda-2c58-48ca-9372-4f9ade69a654.png)

4. *python main.py analytics longest-habit-streak-byhabit*

  To display the longest streak for the habit selected, enter the habit name:
  
  ![image](https://user-images.githubusercontent.com/10673190/226427736-835bd1eb-5aff-4dda-9360-e57432f87155.png)


# Test

The application use *pytest* to execute unit test, please make sure to install and setup in your IDE tool.

There are two python scripts to test the habit and the analytics function:

**To test the habit** one use the following command from the terminal to trigger all tests:
*python -m pytest test_habit.py*

Its possibile to call individual function to test single functionalities:

1. Database table creation test:

*python -m pytest test_habit.py::test_create_db

2. Habit creation test:

*python -m pytest test_habit.py::test_habit_creation*

3. Mark habit as completed test:

*python -m pytest test_habit.py::test_mark_habit_completed*

4. Delete an habit:

*python -m pytest test_habit.py::test_habit_deletion*

**To test the analytics** one use the following command from the terminal to trigger all tests:
*python -m pytest test_analytics.py*

Its possibile to call individual function to test single functionalities:

1. Longest habit streak test:

*python -m pytest test_analytics.py::test_longest_habit_streak*

2. Display habits by periodicity test:

*python -m pytest test_analytics.py::test_get_habits_byperiod*

3. Display all habits test:

*python -m pytest test_analytics.py::test_display_all_habits*

4. Longest habit streak by habit name test:

*python -m pytest test_analytics.py::test_longest_habit_streak_byhabit*


  








  
  


# Get all records from Habit main table
def select_all(conn, query):
    cur = conn.cursor()
    try:
        cur.execute(query)
    except Exception as e:
        print(e)

    rows = cur.fetchall()

    return rows

import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()


def create_table(table_name):
    drop_table(table_name)
    c.execute('CREATE TABLE ' + table_name + ' (module_name TEXT, grade INTEGER)')
    return table_name


def insert_grades_into_table(table_name, module_name, grade):
    c.execute("INSERT INTO " + table_name + " VALUES (?, ?)", (module_name, grade))
    conn.commit()


def drop_table(table_name):
    c.execute("DROP TABLE IF EXISTS " + table_name)
    conn.commit()


def check_if_table_exists(table_name):
    try:
        c.execute("SELECT * FROM " + table_name)
        conn.commit()
        return True
    except sqlite3.OperationalError:
        return False


def get_grades_from_table(table_name):
    year_grades = []
    table = c.execute("SELECT * FROM " + table_name)
    for row in table:
        print(row[1])
        year_grades.append(row[1])

    return year_grades

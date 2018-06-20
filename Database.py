import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()


def create_table(table_name):
    c.execute('CREATE TABLE IF NOT EXISTS ' + table_name + '(module_name TEXT, grade INTEGER) ')
    delete_existing_records_in(table_name)
    return table_name


def insert_grades_into_table(table_name, module_name, grade):
    c.execute("INSERT INTO " + table_name + " VALUES (?, ?)", (module_name, grade))
    conn.commit()


def delete_existing_records_in(table_name):
    c.execute("delete from " + table_name)
    conn.commit()


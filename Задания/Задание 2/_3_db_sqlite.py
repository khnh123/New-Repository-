
# Задание 2

# 1. find name of the exchanger in the database
# 2. extract link

import sqlite3


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        print("Connected to %s" % db_file)
    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    return conn


def extract_link(exchanger_name, table, cur):
    """
    :param exchanger_name: string
    :param table: database table
    :param cur: conn.cursor()
    :return: link (string)
    """
    cur.execute("SELECT Отзывы FROM %s WHERE Обменик=?" % table, (exchanger_name,))
    rows = cur.fetchall()
    for row in rows:
        #print(row[0])
        pass
    return row[0]


def print_all(table, cur):
    """
    :param table: database table
    :param cur: conn.cursor()
    :return: void
    """
    # print all
    sql_select = ''' SELECT * FROM %s ''' % table
    cur.execute(sql_select)
    for row in cur.fetchall():
        print(row)


def get_table_names(cur):
    """
    get the name of the table
    :param cur:
    :return: string or list
    """
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
    available_table = cur.fetchall()
    table = available_table[0][0]
    return table


def get_colomns(cur):
    """
    list of colomns
    get the name of the table
    :param cur:
    :return: string or list
    """
    cur.execute('SELECT * FROM  %s' % table)
    names = list(map(lambda x: x[0], cur.description))
    # print(names)
    return names

def main():
    db_file = 'data1.db'
    conn = create_connection(db_file)
    cur = conn.cursor()

    # get the name of the table
    table = get_table_names(cur)

    exchanger_name = 'Касса'
    extract_link(exchanger_name, table, cur)





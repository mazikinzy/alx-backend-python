#!/usr/bin/python3

import sqlite3

connection = "ALX_prodev.sql"
table = """
CREATE TABLE IF NOT EXISTS user_data (
    user_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    age DECIMAL NOT NULL
);
"""

def create_database(connection):
    conn = sqlite3.connect(connection)
    cursor = conn.cursor()
    return conn, cursor


def create_insert_table(cursor, k):
    cursor.execute(k)


def fetch_all(cursor, rows):
    cursor.execute(rows)
    return cursor.fetchall()


def disconnect(conn):
    conn.close()


def commit(conn):
    conn.commit()


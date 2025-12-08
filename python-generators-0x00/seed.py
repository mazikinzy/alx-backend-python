#!/usr/bin/python3

import sqlite3


def create_database(n):
    conn = sqlite3.connect(n)
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

def run():
    print("Running the program")

#!/usr/bin/python3

import sqlite3

data_base = """
    CREATE DATABASE IF NOT EXISTS ALX_prodev;
"""
table = """
CREATE TABLE IF NOT EXISTS user_data (
    user_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    age DECIMAL NOT NULL
);
"""
table_data = 'C:\\Users\\mazik\\Desktop\\Tech\\user_data.csv'

def connect_db():
    conn = sqlite3.connect(data_base)
    cursor = conn.cursor()
    return conn, cursor


def create_database(connection):
    conn = sqlite3.connect(connection)
    conn.close()


def connect_to_prodev():
    conn = sqlite3.connect("ALX_prodev")
    cursor = conn.cursor()
    return conn, cursor


def create_table(connection):
    conn = sqlite3.connect("ALX_prodev")
    cursor = conn.cursor()
    cursor.execute(table)


def insert_data(connection, data):
    connection = create_table(connection)
    data = table_data
    cursor.execute(
    "INSERT INTO connection (user_name, email, age) VALUES (data)"
)


def fetch_all(cursor, rows):
    cursor.execute(rows)
    return cursor.fetchall()


def disconnect(conn):
    conn.close()


def commit(conn):
    conn.commit()


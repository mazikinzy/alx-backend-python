#!/usr/bin/python3

import sqlite3

data = "user_data.csv"

def connect_db():
    conn = sqlite3.connect('ALX_prodev')
    cursor = conn.cursor()
    return conn, cursor


def create_database(con):
    cursor = con.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")


def connect_to_prodev():
    return conn


def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_data (
        user_id INTEGER AUTO_INCREMENT PRIMARY KEY,
        user_name VARCHAR NOT NULL,
        email VARCHAR NOT NULL,
        age DECIMAL NOT NULL
        );
        """
    )


def insert_data(conn, data):
    cursor = conn.cursor()
    cursor.execute(
    "INSERT INTO connection (user_name, email, age) VALUES (data)"
    )
    conn.commit()
    conn.close()


def disconnect():
    conn.close()


def commit():
    conn.commit()


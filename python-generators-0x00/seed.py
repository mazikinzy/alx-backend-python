#!/usr/bin/python3

import sqlite3

conn = "ALX_prodev.sql"
cursor = conn.cursor()

def create_database(n)
    conn = sqlite3.connect(n)
    return conn

cursor = 

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
        user_id INTEGER PRIMARY KEY,
        user_name VARCHAR(40) NOT NULL,
        email TEXT NOT NULL,
        age DECIMAL NOT NULL
);
""")

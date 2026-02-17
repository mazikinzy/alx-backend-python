#!/usr/bin/python3

import sqlite3

data = "user_data.csv"

def connect_db():
    connection = sqlite3.connect('ALX_prodev')
    connection.close()


def create_database():
    connection = sqlite3.connect('ALX_prodev')
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
    
    cursor.commit()
    cursor.close()


def connect_to_prodev():
    connection = sqlite3.connect('ALX_prodev')
    cursor = connection.cursor()


def create_table():
    connection = sqlite3.connect('ALX_prodev')
    cursor = connnnection.cursor()
    cursor.execute(CREATE TABLE IF NOT EXISTS user_data (
        user_id INTEGER AUTO_INCREMENT PRIMARY KEY,
        user_name VARCHAR NOT NULL,
        email VARCHAR NOT NULL,
        age DECIMAL NOT NULL
        )
    )
    
    cursor.commit()
    cursor.close()


def insert_data():
    connection = sqlite3.connect('ALx_prodev')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO user_data (user_name, email, age) VALUES (data)")

    conn.commit()
    conn.close()


def disconnect():
    conn.close()


def commit():
    conn.commit()


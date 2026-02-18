#!/usr/bin/python3

import sqlite3

data = "python-generators-0x00/user_data.csv"
connection = sqlite3.connect('ALX_prodev')

def connect_db():
    connection = sqlite3.connect('ALX_prodev')


def create_database():
    connection = sqlite3.connect('ALX_prodev')
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    
    connection.commit()


def connect_to_prodev():
    connection = sqlite3.connect('ALX_prodev')
    cursor = connection.cursor()


def create_table():
    connection = sqlite3.connect('ALX_prodev')
    cursor = connnnection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS user_data(
        user_id INTEGER AUTO_INCREMENT PRIMARY KEY,
        user_name VARCHAR NOT NULL,
        email VARCHAR NOT NULL,
        age DECIMAL NOT NULL
        )"
    )
    
    connection.commit()


def insert_data(data):
    connection = sqlite3.connect('ALx_prodev')
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO user_data(user_name, email, age) VALUES (?, ?, ?)", data)

    connection.commit()


def disconnect():
    connection = sqlite3.connect('ALx_prodev')
    connection.close()


def commit():
    connection = sqlite3.connect('ALx_prodev')
    connection.commit()


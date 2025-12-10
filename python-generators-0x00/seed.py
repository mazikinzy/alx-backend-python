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
table_data = ("INSERT INTO user_data (user_name, email, age) VALUES
("Johnnie Mayer","Ross.Reynolds21@hotmail.com", 35),
("Myrtle Waters","Edmund_Funk@gmail.com", 99),
("Flora Rodriguez I","Willie.Bogisich@gmail.com", 84),
("Dr. Cecilia Konopelski-Lakin","Felicia75@gmail.com", 87),
("Chelsea Boyle-Stoltenberg","Regina.Emard97@yahoo.com", 83),
("Seth Mraz","Cecilia_Blanda89@gmail.com", 24),
("Thelma Kris-Schinner","Johnnie.Jast93@hotmail.com", 64),
("Thomas Hane","Dominic24@yahoo.com", 93),
("Della Hickle","Leon_Rohan@hotmail.com", 35),
("Kristi Durgan","Maria_Schmeler9@hotmail.com", 70),
("Brad Sawayn","Tyler.Dach57@gmail.com", 112),
("Isabel Crist Jr.","Cecilia_Braun54@yahoo.com", 63),
("Allen Roob","Sandra.Heidenreich4@yahoo.com", 40),
("Robin Wilkinson","Brent_Wilkinson2@hotmail.com", 62),
("Martin Flatley","Gabriel23@hotmail.com", 13),
("Delia Walker IV","Leticia_Schinner@yahoo.com", 78),
("Blanca Durgan","Christina27@gmail.com", 19),
("Ellen Hudson","Matthew.Medhurst69@gmail.com", 111),
("Bobby Bayer","Erick_Brekke36@gmail.com", 110),
("Karen Pfannerstill","Amber.Steuber-Greenfelder@gmail.com", 49),
("Vanessa Kihn-Durgan","Lorena.Schuppe@hotmail.com", 49),
("Grace Sporer","George38@yahoo.com", 50),
("Krista Herzog-Paucek","Shawn.Tremblay@hotmail.com", 109),
("Doyle Schaden","Clarence.Berge@hotmail.com", 30),
("Beth Crooks","Sean.Bradtke99@yahoo.com", 36),
("Doyle Botsford","Wilfred.Dickinson@hotmail.com", 70),
("Santos Skiles","Joey22@gmail.com", 17),
("Ms. Gina Kuhic","Debbie83@hotmail.com", 78),
("Garry Pfeffer","Lora_Heathcote91@yahoo.com", 105),
("Annie Rogahn","June.Kuhn24@hotmail.com", 92),
("Hubert Gerlach","Alice99@hotmail.com", 3),
("Clark Willms","Leo25@gmail.com", 45),
("Natalie Lesch PhD","Marilyn76@yahoo.com", 76),
("Pauline Cremin","Geraldine.Langworth27@hotmail.com", 50),
("Nellie Labadie","Clay75@hotmail.com", 27),
("Felipe Barrows","Clint37@yahoo.com", 47),
("Derrick Mitchell Jr.","Mark_Fritsch67@hotmail.com", 52),
("James Boehm","Terry9@hotmail.com", 54),
("Darrin Fritsch","Leland.Mills@yahoo.com", 50),
("Blanca Osinski","Annette56@yahoo.com", 96),
("Inez Walker","Fannie_Wolff-Schinner@gmail.com", 19),
("Deanna Kunze","Colleen.Hayes@gmail.com", 109)")


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


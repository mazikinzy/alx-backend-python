#!/usr/bin/python3

def stream_users():
    files = open('user_data.csv', 'r')
    try:
        for rows in files
            yield rows
    finally:
        files.close()

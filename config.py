import sqlite3

USER = [1817004105, 512060643]

TOKEN ='6163180214:AAGnZJ2ZWhm87-0pWDMssxA7QDRDgTQyMmA'

with sqlite3.connect('server.db') as db:
        cursor = db.cursor()
        query = """ CREATE TABLE IF NOT EXISTS users(id INTEGER, name TEXT) """
        cursor.execute(query)

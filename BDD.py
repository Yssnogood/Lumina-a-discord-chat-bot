import sqlite3
import random
from datetime import datetime

conn = sqlite3.connect('memory.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS memory
             (id INTEGER PRIMARY KEY, user_id TEXT, user_msg TEXT,ia_answer TEXT, date DATATIME)''')


def add_conversation(user_id, message, answer):

    conn = sqlite3.connect('memory.db')
    c = conn.cursor()

    c.execute("INSERT INTO memory VALUES (NULL, ?, ?, ?, ?)", (user_id, message,answer,  datetime.now().strftime("%Y-%m-%d%H:%M:%S")))
    conn.commit()
    conn.close()

def remove_users(user):
    conn = sqlite3.connect('memory.db')
    c = conn.cursor()
    # Delete un id
    c.execute("DELETE FROM memory WHERE user_id =?", (user,))
    conn.commit()

    conn.close()

def get_users():
    conn = sqlite3.connect('memory.db')
    c = conn.cursor()
    c.execute("SELECT DISTINCT user_id FROM memory")
    users = c.fetchall()
    conn.close()
    return users

def get_last_conversation(user_id):

    conn = sqlite3.connect('memory.db')
    c = conn.cursor()

    c.execute("SELECT * FROM memory WHERE user_id = ?", (user_id,))
    last_conversation = c.fetchone()
    conn.close()
    return last_conversation

def get_all_conversation(user_id):

    conn = sqlite3.connect('memory.db')
    c = conn.cursor()
    c.execute("SELECT * FROM memory WHERE user_id = ?", (user_id,))
    last_conversation = c.fetchall()
    conn.close()
    return last_conversation


conn.close()

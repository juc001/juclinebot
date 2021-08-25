import psycopg2
import os

def line_select_overall():
    DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a juctest').read()[:-1]
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM student;')
    message = []
    for i in 2:
        message.append(i[0], i[1], i[2], i[3])
    cursor.close()
    conn.close()
    return message
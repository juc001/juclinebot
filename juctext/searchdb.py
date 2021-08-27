import psycopg2
import os
from linebot.models import *

def line_select_overall(event):
    textnum=event.message.text
    num=textnum.split(' ')
    DATABASE_URL =os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    postgres_select_query = f"""SELECT * FROM student;"""
    cursor.execute(postgres_select_query)
    raw = cursor.fetchmany(int(num[1]))
    message = []
    for i in raw:
        message.append((str(i[0]), str(i[1]), str(i[2]),str(i[3])))
    cursor.close()
    conn.close()
    return message
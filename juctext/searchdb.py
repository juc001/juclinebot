import psycopg2
import os
from linebot.models import *

def line_select_overall():
    print('查詢失敗了')
    DATABASE_URL =os.environ['DATABASE_URL']
    print(DATABASE_URL)
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM STUDENT;')
    message=[]
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()
        message.append(row)
    print(message)
    cursor.close()
    conn.close()
    return message
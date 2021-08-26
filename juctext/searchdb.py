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
    for i in range(2):
        temp = cursor.fetchone()
        message.append(temp)
        print('這是第'+i+'行')
    print('總共:'+message)
    cursor.close()
    conn.close()
    return message
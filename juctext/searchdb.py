import psycopg2
import os
from linebot.models import *

def line_select_overall():
    print('查詢失敗了')
    DATABASE_URL =os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM student;')
    message=[]
    for i in range(2):
        message.append(str(i[0]), str(i[1]), str(i[2]), str(i[3]))
        print('這是第'+i+'行')
    cursor.close()
    conn.close()
    return message
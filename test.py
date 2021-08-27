import os
import psycopg2
DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a juctest').read()[:-1]

textnum='查詢 3'
num=textnum.split(' ')
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()
postgres_select_query = f"""SELECT * FROM student;"""
cursor.execute(postgres_select_query)
raw = cursor.fetchmany(int(num[1]))
message = []
for i in raw:
    message.append([str(i[0]), str(i[1]), str(i[2]),str(i[3])])
cursor.close()
conn.close()
print(message)
print(type(message))
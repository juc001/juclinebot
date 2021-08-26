import os
import psycopg2

DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a juctest').read()[:-1]
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()
cursor.execute("SELECT * FROM student")
data = []
while True:
    temp = cursor.fetchone()
    if temp:
        data.append(temp)
    else:
        break
    print(data)
import psycopg2
import os

def line_select_overall():
    DATABASE_URL = 'postgres://npiqezewrkddpe:0a97822788672e9ee3a0521b75427bf4d0b92f20e5fda20b44ebe3bf1128bc9d@ec2-18-214-238-28.compute-1.amazonaws.com:5432/d4u1bgq5fsb3a'

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    
    postgres_select_query = f"""SELECT * FROM student;"""
    
    cursor.execute(postgres_select_query)
    raw = cursor.fetchmany(2)
    message = []
    
    for i in raw:
        message.append((i[0], i[1], i[2], i[3]))
    
    cursor.close()
    conn.close()
    
    return message
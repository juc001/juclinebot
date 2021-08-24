import psycopg2
import os

def line_select_overall(fetchnumber):
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    
    postgres_select_query = f"""SELECT * FROM student;"""
    
    cursor.execute(postgres_select_query)
    raw = cursor.fetchmany(int(fetchnumber))
    message = []
    
    for i in raw:
        message.append((i[0], i[1], i[2], str(i[3])[:-3], str(i[4])))
    
    cursor.close()
    conn.close()
    
    return message
import psycopg2
import os


def line_insert_record(record_list):
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    table_columns = '(id, name, gender, grade)'
    postgres_insert_query = f"""INSERT INTO sudent {table_columns} VALUES (%s,%s,%s,%s)"""

    cursor.executemany(postgres_insert_query, record_list)
    conn.commit()

    message = f"恭喜您！ {cursor.rowcount} 筆資料成功匯入 sudent 表單！"
    print(message)

    cursor.close()
    conn.close()
    
    return message


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
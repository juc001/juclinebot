import psycopg2
from linebot.models import *

#紀錄主程式
line_bot_api = '1oBwTrLvaEqSse8SULJUFmSzGSrV2NWxr71/pgCjKqUs+jaNZ2iktP+8sU0ZxSNNr/CZrgT8GUcetwRo+PeUaG0L90LBTgrr43UesgCI6IjmyuusaVtbuhrmsoA8G/nndtQ49fw28V4opCDuL/Df4QdB04t89/1O/w1cDnyilFU='
def insert_record(event):
    
    if '學生紀錄' in event.message.text:
        
        try:
            record_list = prepare_record(event.message.text)
            reply = line_insert_record(record_list)

            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=reply)
            )

        except:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='失敗了')
            )

        return True
    else:
        return False
#準備資料
def prepare_record(text):
    text_list = text.split('\n')
    record_list = []
    for i in text_list[1:]:
        temp_list = i.split(',')
        temp_id = temp_list[0]
        temp_name = temp_list[1]
        temp_gender = temp_list[2]
        temp_grade = temp_list[3]
        record = (temp_id, temp_name, temp_gender, temp_grade)
        record_list.append(record)
    TextSendMessage(text='準備資料')
    return record_list
#紀錄過程
def line_insert_record(record_list):
    DATABASE_URL = 'postgres://npiqezewrkddpe:0a97822788672e9ee3a0521b75427bf4d0b92f20e5fda20b44ebe3bf1128bc9d@ec2-18-214-238-28.compute-1.amazonaws.com:5432/d4u1bgq5fsb3a'

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    table_columns = '(id, name, gender, grade)'
    postgres_insert_query = f"""INSERT INTO sudent {table_columns} VALUES (%s,%s,%s,%s)"""

    cursor.executemany(postgres_insert_query, record_list)
    conn.commit()
    TextSendMessage(text='過程')
    message = f"恭喜您！ {cursor.rowcount} 筆資料成功匯入 sudent 表單！"
    print(message)

    cursor.close()
    conn.close()
    
    return message



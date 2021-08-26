import psycopg2,os
from linebot.models import *

#紀錄主程式
line_bot_api = '1oBwTrLvaEqSse8SULJUFmSzGSrV2NWxr71/pgCjKqUs+jaNZ2iktP+8sU0ZxSNNr/CZrgT8GUcetwRo+PeUaG0L90LBTgrr43UesgCI6IjmyuusaVtbuhrmsoA8G/nndtQ49fw28V4opCDuL/Df4QdB04t89/1O/w1cDnyilFU='
def insert_record(event):
    remessages=TextSendMessage(text='if失敗了')
    if '學生紀錄' in event.message.text:
        try:
            record_list = prepare_record(event.message.text)
            print('prepare_record end')
            reply = line_insert_record(record_list)
            print('line_insert_record end')
            remessages=TextSendMessage(text=reply)
        except:
            remessages=TextSendMessage(text='匯入失敗了')
    return remessages
#準備資料
def prepare_record(text):
    print('prepare_record')
    text_list = text.split('\n')
    print(text_list)
    record_list=[]
    print('FOR上')
    for i in text_list[1:]:
        temp_list = i.split(' ')
        print(temp_list)
        temp_id = temp_list[0]
        print(temp_id)
        temp_name = temp_list[1]
        print(temp_name)
        temp_gender = temp_list[2]
        print(temp_gender)
        temp_grade = temp_list[3]
        print(temp_grade)
        print('record下:'+i)
        record_list.append[temp_id,temp_name,temp_gender,temp_grade]
        print('加入:'+record_list)
    return record_list
#紀錄過程
def line_insert_record(record_list):
    print('line_insert_record')
    DATABASE_URL = os.environ['DATABASE_URL']
    print('DATABASE_URL連線1')
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    print('DATABASE_URL連線2')
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO sudent(id, name, gender, grade) VALUES (%s,%s,%s,%s)', record_list)
    print('資料輸入')
    conn.commit()
    print('資料允許')
    message =("恭喜您！"+ {cursor.rowcount}+" 筆資料成功匯入 sudent 表單！")
    print(message)
    cursor.close()
    conn.close()
    return message



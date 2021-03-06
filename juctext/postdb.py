import psycopg2,os
from linebot.models import *

#紀錄主程式
line_bot_api = '1oBwTrLvaEqSse8SULJUFmSzGSrV2NWxr71/pgCjKqUs+jaNZ2iktP+8sU0ZxSNNr/CZrgT8GUcetwRo+PeUaG0L90LBTgrr43UesgCI6IjmyuusaVtbuhrmsoA8G/nndtQ49fw28V4opCDuL/Df4QdB04t89/1O/w1cDnyilFU='
def insert_record(event):
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
    text_list = text.split('\n')
    record_list=[]
    for i in text_list[1:]:
        temp_list = i.split(' ')
        temp_id = temp_list[0]
        temp_name = temp_list[1]
        temp_gender = temp_list[2]
        temp_grade = temp_list[3]
        prerecord=(temp_id,temp_name,temp_gender,temp_grade)
        record_list.append(prerecord)        
    return record_list
#紀錄過程
def line_insert_record(record_list):
    DATABASE_URL =os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    jucinsert="INSERT INTO STUDENT(id, name, gender, grade) VALUES (%s,%s,%s,%s)"
    cursor.executemany(jucinsert, record_list)
    conn.commit()
    num=cursor.rowcount
    message =("恭喜您！"+str(num)+" 筆資料成功匯入 sudent 表單！")
    print(message)
    cursor.close()  
    conn.close()
    return message



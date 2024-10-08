from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from juctext import msgtext,searchdb,postdb


#======這裡是呼叫的檔案內容=====

#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import os


#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi(os.getenv('CHANNEL_ACCESS_TOKEN'))
# Channel Secret
handler = WebhookHandler(os.getenv('CHANNEL_SECRET'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    #顯示內容
    print(body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '組圖' in msg:
        message = msgtext.imagemap_message()
    elif '學生紀錄' in msg:
        message =postdb.insert_record(event)
    elif '查詢' in msg:
        message = searchdb.line_select_overall(event)
    elif '按鈕' in msg:
        message = msgtext.buttons_message()
    elif '確認' in msg:
        message = msgtext.Confirm_Template()
    elif '旋轉木馬' in msg:
        message = msgtext.Carousel_Template()
    elif '圖片畫廊' in msg:
        message = msgtext.image_carousel_message1()
    elif '功能' in msg:
        message = msgtext.func_list()
    elif '表情' in msg:
        message =msgtext.emoji_text()
    elif '圖片' in msg:
        message =msgtext.Image_Send()
    elif '影片' in msg:
        message =msgtext.Video_Send()
    elif '音檔' in msg:
        message =msgtext.Audio_Send()
    elif '地址' in msg:
        message =msgtext.Location_Send()
    elif '貼圖' in msg:
        message =msgtext.Sticker_Send()
    else:
        message = msgtext.GPT_response(msg)
    line_bot_api.reply_message(event.reply_token, message)

@handler.add(PostbackEvent)
def handle_message(event):
    print(event.postback.data)


@handler.add(MemberJoinedEvent)
def welcome(event):
    uid = event.joined.members[0].user_id
    gid = event.source.group_id
    profile = line_bot_api.get_group_member_profile(gid, uid)
    name = profile.display_name
    message = TextSendMessage(text=f'{name}歡迎加入')
    line_bot_api.reply_message(event.reply_token, message)
        
        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

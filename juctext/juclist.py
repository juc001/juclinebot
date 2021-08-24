#這個檔案的作用是：建立功能列表

#===============這些是LINE提供的功能套組，先用import叫出來=============
from linebot.models import *
#===============LINEAPI=============================================

#以下是本檔案的內容本文

#1.建立旋轉木馬訊息，名為function_list(未來可以叫出此函數來使用)
#function_list的括號內是設定此函數呼叫時需要給函數的參數有哪些

def function_list():
  message = {
  "type": "bubble",
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "最新合作廠商",
          "data": "最新合作廠商",
          "displayText": "最新合作廠商"
        },
        "color": "#DDA0DD"
      },
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "活動消息",
          "data": "活動消息",
          "displayText": "活動消息"
        },
        "color": "#BA55D3"
      },
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "註冊會員",
          "data": "註冊會員",
          "displayText": "註冊會員"
        },
        "color": "#4B0082"
      },
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "旋轉木馬",
          "data": "旋轉木馬",
          "displayText": "旋轉木馬"
        },
        "color": "#FF69B4"
      },
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "圖片畫廊",
          "data": "圖片畫廊",
          "displayText": "圖片畫廊"
        },
        "color": "#C71585"
      },
      {
        "type": "spacer",
        "size": "sm"
      }
    ],
    "flex": 0
  }
  }
  return message
#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
import json

#ImagemapSendMessage(組圖訊息)
def imagemap_message():
    message= ImagemapSendMessage(
    base_url='https://th.bing.com/th/id/OIP.d-gWntZuq3XavU5xbsiACwHaHa?pid=ImgDet&rs=1',
    alt_text='this is an imagemap',
    base_size=BaseSize(height=520, width=520),
    video=Video(
        original_content_url='https://dl259.dlmate16.xyz/?file=M3R4SUNiN3JsOHJ6WVo3MXN2Mlg5WVM5RkYrNHVyaHAwK1l5eGhRc0ZyZ0hqb0k2eE9IckJzZExKNmtJaHF5M0hkSWYyei9SZjlHQ2V6Mk11YlluQ1ZhdjBKME9yRDN3NWR4MENmay9Xd2FzM2VDcW1qUkptUWJoZG9XSVI1NVBZbUp2dGtKbWxuUzF3ZUdBL0VmZTRUai9nVlRSWVNVZXQzVUlNdmlidk5SYjNXalBZT0QzN0pnS3VEV2EzWjlIM3ZtVHN6N3cxcjR5aDlKMFYwcDFlcTlQM0pYNzNzL0pxMEFtazR3ZTVXUzhyczZjSkxZRkJJMnpSaUVpYW5JNXArTC9DRjBiMXpVWDZtbXEvNklnc3pGZkl2RWh2VFRub2FDdmRUYUNlNStuR3NYZGVMSHI0TmJ2ditwMzdSVT0%3D',
        preview_image_url='https://s3.amazonaws.com/lowres.jantoo.com/animal-kingdom-play-playing-eels-electric_eels-fish-08332490_low.jpg',
        area=ImagemapArea(
            x=0, y=0, width=520, height=290
        ),
        external_link=ExternalLink(
            link_uri='https://www.youtube.com/watch?v=eb9EqoKPV90',
            label='See More',
        ),
    ),
    actions=[
        URIImagemapAction(
            link_uri='https://www.facebook.com/',
            area=ImagemapArea(
                x=0, y=0, width=260, height=520
                )
            ),
        MessageImagemapAction(
            text='hello',
            area=ImagemapArea(
                x=260, y=0, width=260, height=520
                )
            )
        ]
    )   
    return message
#TemplateSendMessage - ButtonsTemplate (按鈕介面訊息)
def buttons_message():
    message = TemplateSendMessage(
        alt_text='好消息來囉～',
        template=ButtonsTemplate(
            thumbnail_image_url="https://pic2.zhimg.com/v2-de4b8114e8408d5265503c8b41f59f85_b.jpg",
            title="是否要進行抽獎活動？",
            text="輸入生日後即獲得抽獎機會",
            actions=[
                DatetimePickerTemplateAction(
                    label="請選擇生日",
                    data="input_birthday",
                    mode='date',
                    initial='1990-01-01',
                    max='2019-03-10',
                    min='1930-01-01'
                ),
                MessageTemplateAction(
                    label="看抽獎品項",
                    text="有哪些抽獎品項呢？"
                ),
                URITemplateAction(
                    label="免費註冊享回饋",
                    uri="https://tw.shop.com/nbts/create-myaccount.xhtml?returnurl=https%3A%2F%2Ftw.shop.com%2F"
                )
            ]
        )
    )
    return message
#TemplateSendMessage - ConfirmTemplate(確認介面訊息)
def Confirm_Template():

    message = TemplateSendMessage(
        alt_text='是否註冊成為會員？',
        template=ConfirmTemplate(
            text="是否註冊成為會員？",
            actions=[
                PostbackTemplateAction(
                    label="馬上註冊",
                    text="現在、立刻、馬上",
                    data="會員註冊"
                ),
                MessageTemplateAction(
                    label="查詢其他功能",
                    text="查詢其他功能"
                )
            ]
        )
    )
    return message
#旋轉木馬按鈕訊息介面
def Carousel_Template():
    message = TemplateSendMessage(
        alt_text='一則旋轉木馬按鈕訊息',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Number_1_in_green_rounded_square.svg/200px-Number_1_in_green_rounded_square.svg.png',
                    title='這是第一塊模板',
                    text='一個模板可以有三個按鈕',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='將這個訊息偷偷回傳給機器人'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是1'
                        ),
                        URITemplateAction(
                            label='進入1的網頁',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Number_1_in_green_rounded_square.svg/200px-Number_1_in_green_rounded_square.svg.png'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuo7n2_HNSFuT3T7Z9PUZmn1SDM6G6-iXfRC3FxdGTj7X1Wr0RzA',
                    title='這是第二塊模板',
                    text='副標題可以自己改',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='這是ID=2'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是2'
                        ),
                        URITemplateAction(
                            label='進入2的網頁',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Number_2_in_light_blue_rounded_square.svg/200px-Number_2_in_light_blue_rounded_square.svg.png'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Number_3_in_yellow_rounded_square.svg/200px-Number_3_in_yellow_rounded_square.svg.png',
                    title='這是第三個模塊',
                    text='最多可以放十個',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='這是ID=3'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是3'
                        ),
                        URITemplateAction(
                            label='uri2',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Number_3_in_yellow_rounded_square.svg/200px-Number_3_in_yellow_rounded_square.svg.png'
                        )
                    ]
                )
            ]
        )
    )
    return message
#TemplateSendMessage - ImageCarouselTemplate(圖片旋轉木馬)
def image_carousel_message1():
    message = TemplateSendMessage(
        alt_text='圖片旋轉木馬',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/uKYgfVs.jpg",
                    action=URITemplateAction(
                        label="新鮮水果",
                        uri="http://img.juimg.com/tuku/yulantu/110709/222-110F91G31375.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QOcAvjt.jpg",
                    action=URITemplateAction(
                        label="新鮮蔬菜",
                        uri="https://cdn.101mediaimage.com/img/file/1410464751urhp5.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/Np7eFyj.jpg",
                    action=URITemplateAction(
                        label="可愛狗狗",
                        uri="http://imgm.cnmo-img.com.cn/appimg/screenpic/big/674/673928.JPG"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QRIa5Dz.jpg",
                    action=URITemplateAction(
                        label="可愛貓咪",
                        uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                )
            ]
        )
    )
    return message
#建立功能列表
def func_list():
    remessage = TextSendMessage(text='組圖 \n按鈕\n確認\n旋轉木馬\n圖片畫廊\n學生紀錄:\nID 名字 性別 年紀\n查詢 數量\n表情\n圖片\n影片\n音檔\n地址\n貼圖')
    return remessage
#emoji實驗
def emoji_text():
    emoji = [
    {
        "index": 0,
        "productId": "5ac1bfd5040ab15980c9b435",
        "emojiId": "001"
    },
    {
        "index": 14,
        "productId": "5ac1bfd5040ab15980c9b435",
        "emojiId": "002"
    }
    ]
    text_message = TextSendMessage(text='$ LINE emoji  $', emojis=emoji)
    return text_message
#圖片實驗
def Image_Send():
    image_message = ImageSendMessage(
    original_content_url='https://th.bing.com/th/id/OIP.C-kOjyzl0RYV6Ztl6msogQHaD4?pid=ImgDet&rs=1',
    preview_image_url='https://th.bing.com/th/id/OIP.asdpsCTwQqvUQMTjpu7xQwHaIO?pid=ImgDet&w=400&h=444&rs=1'
    )
    return image_message
#影片實驗
def Video_Send():
    video_message = VideoSendMessage(
    original_content_url='https://dl259.dlmate16.xyz/?file=M3R4SUNiN3JsOHJ6WVo3MXN2Mlg5WVM5RkYrNHVyaHAwK1l5eGhRc0ZyZ0hqb0k2eE9IckJzZExKNmtJaHF5M0hkSWYyei9SZjlHQ2V6Mk11YlluQ1ZhdjBKME9yRDN3NWR4MENmay9Xd2FzM2VDcW1qUkptUWJoZG9XSVI1NVBZbUp2dGtKbWxuUzF3ZUdBL0VmZTRUai9nVlRSWVNVZXQzVUlNdmlidk5SYjNXalBZT0QzN0pnS3VEV2EzWjlIM3ZtVHN6N3cxcjR5aDlKMFYwcDFlcTlQM0pYNzNzL0pxMEFtazR3ZTVXUzhyczZjSkxZRkJJMnpSaUVpYW5JNXArTC9DRjBiMXpVWDZtbXEvNklnc3pGZkl2RWh2VFRub2FDdmRUYUNlNStuR3NYZGVMSHI0TmJ2ditwMzdSVT0%3D',
    preview_image_url='https://s3.amazonaws.com/lowres.jantoo.com/animal-kingdom-play-playing-eels-electric_eels-fish-08332490_low.jpg'
    )
    return video_message
#音檔實驗
def Audio_Send():
    audio_message = AudioSendMessage(
    original_content_url='https://freepd.com/music/Beat%20Thee.mp3',
    duration=240000
    )
    return audio_message
#地址實驗
def Location_Send():
    location_message = LocationSendMessage(
    title='猜猜這是哪',
    address='地址喔',
    latitude=35.65910807942215,
    longitude=139.70372892916203)
    return location_message
#貼圖實驗
def Sticker_Send():
    sticker_message = StickerSendMessage(
    package_id='1',
    sticker_id='1')
    return sticker_message

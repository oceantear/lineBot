from linebot import LineBotApi

from linebot.models import (
    TextSendMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackAction, MessageAction, URIAction,
    CarouselTemplate, CarouselColumn, LocationSendMessage, AudioSendMessage, StickerSendMessage, VideoSendMessage)
from linebot.exceptions import LineBotApiError

class Demo(object):

    def __init__(self, event):
        self.CHANNEL_ACCESS_TOKEN = ""
        self.to = ""
        self.line_bot_api = LineBotApi(self.CHANNEL_ACCESS_TOKEN)
        self.event = event

    def push_video_msg(self):
        video_message = VideoSendMessage(
            original_content_url='',
            preview_image_url=''
        )

        try:
            self.line_bot_api.reply_message(self.event.reply_token, video_message)
        except LineBotApiError as e:
            # error handle
            raise e

    def img_msg(self):
        image_url = "https://i.guim.co.uk/img/media/22bed68981e92d7a9ff204ed7d7f5776a16468fe/1933_1513_3623_2173/master/3623.jpg?width=605&quality=45&auto=format&fit=max&dpr=2&s=da5b088be9a2aa1527f7509ce6a70c68"    
        img_message = ImageSendMessage(
            original_content_url=image_url, 
            preview_image_url=image_url)

        self.line_bot_api.reply_message(self.event.reply_token, img_message)    
                       

    def location_msg(self):
        location_message = LocationSendMessage(
            title='我的位置',
            address='測試位置',
            latitude=25.144456,
            longitude=121.14610858
        )
        
        self.line_bot_api.reply_message(self.event.reply_token, location_message)

    def audio_msg(self):
        audio_message = AudioSendMessage(
            original_content_url='',
            duration=240000
        )
        self.line_bot_api.reply_message(self.event.reply_token, audio_message)

    def video_msg(self):
        video_message = VideoSendMessage(
            original_content_url='',
            preview_image_url=''
        )

        self.line_bot_api.reply_message(self.event.reply_token, video_message)    

    def stick_msg(self):
        sticker_message = StickerSendMessage(
            package_id='1',
            sticker_id='1'
        )
        self.line_bot_api.reply_message(self.event.reply_token, sticker_message)

    def text_msg(self):
        text_message = TextSendMessage(text='Hello, world')
        self.line_bot_api.reply_message(
            self.event.reply_token,
            text_message)             
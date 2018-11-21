# -*- coding: utf-8 -*-
from wxpy import *


bot = Bot(console_qr=True)
myself = bot.self
my_friend = bot.friends().search(u'Ning')[0]
my_friend.send('got onLine')

tuling = Tuling(api_key='b70e64b5d2334ea88afef4837d1e3014')

@bot.register()
def print_others(msg):
    print(msg)

@bot.register(my_friend)
def reply_my_friend(msg):
    print(msg)
    tuling.do_reply(msg)

@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    # 接受好友请求
    new_friend = msg.card.accept()
    # 向新的好友发送消息
    new_friend.send('哈哈，我自动接受了你的好友请求')

@bot.register(Group, TEXT)
def reply_group_msg(msg):
    print(msg)
    if msg.is_at:
        tuling.do_reply(msg)

embed()

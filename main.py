#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append("/usr/local/python3.6/lib/python3.6/site-packages")
sys.path.append("/usr/local/lib/python3.5/dist-packages")
import telebot
import time
from telebot import types


bot = telebot.TeleBot("REPLACE YOUR TOKEN HERE")

try:
	@bot.message_handler(commands=['greeting'])
	def greeting(message):
		c_time = time.time() + 28800
		c_time = int(c_time % 86400 // 3600)
		if 0<=c_time<5:
			txt = "晚安"
		elif 5<=c_time<11:
			txt = "早上好"
		elif 11<=c_time<14:
			txt = "中午好"
		elif 14<=c_time<18:
			txt = "下午好"
		elif 18<=c_time<22:
			txt = "晚上好"
		elif 22<=c_time<24:
			txt = "晚安"
		send_name = str(message.from_user.first_name)
		if message.reply_to_message == None:
			txt = send_name + " 向 大家 道" + txt + "～"
		else:
			reply_name = str(message.reply_to_message.from_user.first_name)
			if message.reply_to_message.from_user.username == None:
				txt = send_name + " 向 " + reply_name + " 道 " + txt + "～"
			else:
				txt = send_name + " 向 " + reply_name + " 道 " + txt + "～ @" + message.reply_to_message.from_user.username
			if message.reply_to_message.from_user.username == "goodnight_prpr_bot":
				txt = "不需要 给窝 道 打招呼 啦～" 
		bot.send_message(message.chat.id, txt)
		bot.delete_message(message.chat.id, message.message_id)

	bot.polling(none_stop=True)
except KeyboardInterrupt:
    quit()
except Exception as e:
    print(str(e))

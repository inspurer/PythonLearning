#coding=utf8
import itchat

# 当接收到的消息是Text，即文字消息
#注册re_msg的意义在于，告诉itchat每次有符合特定条件的消息，itchat要把消息作为参数，去调用re_msg。
@itchat.msg_register('Text')
def text_reply(msg):
	#message:取出msg里面的文本消息
	message = msg['Text']
	# 回复给好友
	replay = u'肖涛已在电脑上登陆网页微信，但暂时无法进行交流,可以给他发送电脑QQ消息哈'  
	#主要是一些关键词设置
	# if B in A 如果 A中有B的话
	if u'干什么' in message:
		replay = u'在忙呢'
	elif u'逼' in message:
		replay = u'含有敏感词汇,请注意言辞'
	elif u'生气' in message:
		replay = u'生气对身体不好'
	elif u'?' in  message:
		replay = u'哈哈，我也不知道'
	elif u'不理你' in message:
		replay = u'乖，忙完给你买糖吃'
	elif u'涛' in message:
		replay = u'他是我主人'
	elif u'厉害' in message:
		replay = u'不不不，辣鸡一个'
	elif u'你好' in message:
		replay = u'你好哇'
	elif u'好吧' in message:
		replay = u'再见'
	return replay
#弹出扫码登录界面,参数这样设置的好处是短时间内退出程序，再次登录可以不用扫码
itchat.auto_login(hotReload=True)
#开启自动回复
itchat.run()
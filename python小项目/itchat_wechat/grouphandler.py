import itchat
import requests
def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'   #改成你自己的图灵机器人的api
        'key': 'ce697b3fc8b54d5f88c2fa59772cb2cf',  # Tuling Key 
        'info': msg,  # 这是我们发出去的消息
        'userid': 'wechat-robot',  # 这里可随意修改
    }
    # 通过如下命令发送一个post请求
    r = requests.post(apiUrl, data=data).json()
    return r.get('text')
@itchat.msg_register(itchat.content.TEXT)
#用于接收来自朋友间的对话消息  #如果不用这个，朋友发的消息便不会自动回复 
def print_content(msg):
    return get_response(msg['Text'])
#用于接收群里面的对话消息
@itchat.msg_register([itchat.content.TEXT], isGroupChat=True)
def print_content(msg):
    return get_response(msg['Text'])
itchat.auto_login(True)
itchat.run()

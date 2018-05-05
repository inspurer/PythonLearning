import os.path
from flask import Flask
from flask.ext.mail import Mail, Message

app = Flask(__name__)
# you can modify the following configurations to the server of your own email
# if you don't know the server, use www.baidu.com
app.config['MAIL_SERVER'] = 'smtp.126.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
# for example, if your email is abcd@126.com,
# then you should write abcd for the following username configuration
app.config['MAIL_USERNAME'] = 'your own username of your email'
app.config['MAIL_PASSWORD'] = 'your own password of the username'

def sendEmail(From, To, Subject, Body, Html, Attachments):
    '''To:must be a list'''
    msg = Message(Subject, sender=From, recipients=To)
    msg.body = Body
    msg.html = Html
    for f in Attachments:
        with app.open_resource(f) as fp:
            msg.attach(filename=os.path.basename(f),
                       content_type = 'application/octet-stream',
                       data=fp.read())
    mail = Mail(app)
    with app.app_context():
        mail.send(msg)

if __name__=='__main__':
    # note:the from address must be equal to the above username configuration
    From = '<your email address>'
    # ok, this is my email address
    To = ['<306467355@qq.com>']
    Subject = 'hello world'
    Body = 'Only a test.'
    Html = '<h1>test test test.</h1>'
    Attachments =['c:\\python35\\python.exe']
    sendEmail(From, To, Subject, Body, Html, Attachments)

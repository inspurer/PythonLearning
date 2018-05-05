import os
import win32security
import win32con
import win32api

class Impersonate:
    def __init__(self,loginName,password):
        self.domain = 'WORKGROUP'
        self.loginName = loginName
        self.password = password
	
    def logon(self):
        self.handel = win32security.LogonUser(self.loginName,self.domain,self.password,
                                              win32con.LOGON32_LOGON_INTERACTIVE,
                                              win32con.LOGON32_PROVIDER_DEFAULT)
        win32security.ImpersonateLoggedOnUser(self.handel) #假冒别人身份登录系统
        
    def logoff(self):
        win32security.RevertToSelf() #结束模仿，切换至本来的用户名
        print('OK. I am back '+win32api.GetUserName())
        self.handel.Close() #关闭句柄
	
print('Origionally I am '+win32api.GetUserName())
a=Impersonate('ddddd','123456')#要模仿的用户名和密码
try:
    a.logon() #以别人身份登录    
    print('Now I become '+win32api.GetUserName()) #显示当前的登录用户名
    os.mkdir(r'D:\test_ddd\ddd')
    a.logoff() #注销并切换至本来的用户身份    
except:
    print("Denied.Now I will become an administrator and try again")
    a.logoff()
    os.mkdir(r'D:\test_ddd\administrator')

import win32evtlog
import win32evtlogutil
import win32security
import win32con
import winerror
import time
import re
import sys
import traceback
import threading

def date2sec(evt_date):
    '''把类似于'6/26/15 15:54:09'格式的日期时间字符串转换为1970以来经过的秒数'''
    the_date, the_time = evt_date.split()#把日期和时间分开
    (month, day, year) = map(lambda x: int(x), the_date.split(r'/'))
    (hour, minute, second) = map(lambda x: int(x), the_time.split(r':'))
    if 70<year<100:
        year = year+1990
    elif year<50:
        year = year+2000
    tup = (year,month,day,hour,minute,second,0,0,0)
    seconds = time.mktime(tup)
    return seconds

def main(computer='.', logtype='System', interval = 480):
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ|\
            win32evtlog.EVENTLOG_SEQUENTIAL_READ
    evt_dict = {win32con.EVENTLOG_AUDIT_FAILURE:'审核失败事件',
                win32con.EVENTLOG_AUDIT_SUCCESS:'审核成功事件',
                win32con.EVENTLOG_INFORMATION_TYPE:'通知事件',
                win32con.EVENTLOG_WARNING_TYPE:'警告事件',
                win32con.EVENTLOG_ERROR_TYPE:'错误事件'}
    begin_sec = time.time()
    begin_time = time.strftime('%H:%M:%S',time.localtime(begin_sec))
    try:
        hand = win32evtlog.OpenEventLog(computer,logtype)#打开日志
    except:
        print('无法打开"{0}"服务器上的"{1}"日志'.format(computer, logtype))
        return
    print(logtype,' events found in the last {0} hours before {1}'.format(interval/60/60, begin_time))
    
    events = 1
    while events:
        events = win32evtlog.ReadEventLog(hand,flags,0)
        for ev_obj in events:
            try:
                the_time = ev_obj.TimeGenerated.Format('%D %H:%M:%S')
                seconds = date2sec(the_time)
                if seconds < begin_sec-interval: #只查看指定时间段内的日志
                    break
                computer = ev_obj.ComputerName
                cat = str(ev_obj.EventCategory)
                src = str(ev_obj.SourceName)
                record = str(ev_obj.RecordNumber)
                evt_id = str(winerror.HRESULT_CODE(ev_obj.EventID))
                evt_type = evt_dict[ev_obj.EventType]
                msg = win32evtlogutil.SafeFormatMessage(ev_obj, logtype)
                print(':'.join((the_time,computer,src,cat,record,evt_id,evt_type,msg)))
                print('='*20)
                if seconds < begin_sec-interval:
                    break
            except:
                pass
    win32evtlog.CloseEventLog(hand)
 
#多线程支持
##t1 = threading.Thread(target=main, args=('.','Setup',3600))
##t1.start()
##t1.join()
##t2 = threading.Thread(target=main, args=('.', 'Application',7200))
##t2.start()
##t2.join()
t3 = threading.Thread(target=main, args=('.', 'Application',5400))
t3.start()
t3.join()

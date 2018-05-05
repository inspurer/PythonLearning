import socket
import multiprocessing

def ports(ports_service):
    #获取常用端口对应的服务名称
    for port in list(range(1,100))+[143,145,113,443,445,3389, 8080]:
        try:
            ports_service[port] = socket.getservbyport(port)
        except socket.error:
            pass

def ports_scan(host, ports_service):
    ports_open = []
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
    except socket.error:
        print('socket creation error')
        sys.exit()
    for port in ports_service:
        try:
            #尝试连接指定端口
            sock.connect((host,port))
            #记录打开的端口
            ports_open.append(port)
            sock.close()
        except socket.error:
            pass
    return ports_open

if __name__=='__main__':
    m = multiprocessing.Manager()
    ports_service = dict()
    results = dict()
    ports(ports_service)
    #创建进程池，允许最多8个进程同时运行
    pool = multiprocessing.Pool(processes=8)
    net = '10.2.1.'
    for host_number in map(str,range(8,10)):
        host = net+host_number
        #创建一个新进程，同时记录其运行结果
        results[host] = pool.apply_async(ports_scan, (host, ports_service))
        print('starting '+host+'...')
    #关闭进程池，close()必须在join()之前调用
    pool.close()
    #等待进程池中的进程全部执行结束
    pool.join()

    #打印输出结果
    for host in results:
        print('='*30)
        print(host,'.'*10)
        for port in results[host].get():
            print(port, ':', ports_service[port])

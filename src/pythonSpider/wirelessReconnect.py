'''
尝试突破校园网流量限制,通过抓取登录信息
实现无限制流量上网
'''
import socket

def getIP():
    local_ip=socket.gethostbyname(socket.gethostname())
    ip_lists=socket.gethostbyname_ex(socket.gethostname())
    print(local_ip)
    print(ip_lists)

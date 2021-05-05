
# coding = utf-8

import socket
socket.setdefaulttimeout(0.1)

def get_port(host, port):
    try:
        obj = socket.socket()
        obj.connect((host,port))
        return True
    except:
        return False

def port_scan_test():
    if get_port('127.0.0.1',80):
        print('open!!!')
    else:
        print("No No No!!!")

port_scan_test()
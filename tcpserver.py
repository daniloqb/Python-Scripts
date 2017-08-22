import socket
import simplejson as json

__author__ = 'tic'



host = ''
port = 2121
size = 1024
backlog = 5





s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)

while 1:
    client,address = s.accept()
    data = client.recv(size)
    if data:
        print "Server received:", json.dumps(data)

        client.send(data)
    client.close()

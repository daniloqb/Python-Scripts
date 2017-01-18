import socket
import simplejson as json

__author__ = 'tic'

host = '192.168.6.143'
port = 2121
size = 1024

d_json = {'led':'on','rgb':['255','100','50']}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send(json.dumps(d_json))
data = s.recv(1024)
s.close()

j = json.loads(data)

print json.dumps(j,sort_keys=True, indent=4 * '')


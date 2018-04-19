
import simplejson as json
import socket
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import time


hostName = ""
hostPort = 2121

class MyServer(BaseHTTPRequestHandler):
    def do_POST(self):
        print "incomming http", self.path

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.send_response(200)
        self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path))

        j = json.loads(post_data)
        pretty_data = json.dumps(j,sort_keys=True,indent=4 * ' ')
        print pretty_data

myServer = HTTPServer((hostName,hostPort),MyServer)
print time.asctime(), "Server Starts - %s:%s" % (hostName,hostPort)

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print time.asctime(), "Server Stops - %s:%s" %(hostName, hostPort)

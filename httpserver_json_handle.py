
import simplejson as json
import socket
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import time




class MyServer(BaseHTTPRequestHandler):
    def do_POST(self):
        print "incomming http", self.path

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        # Send the html message
        self.wfile.write(json.dumps(json.loads('{"msg":"Hello World"}')))


        j = json.loads(post_data)
        pretty_data = json.dumps(j,sort_keys=True,indent=4 * ' ')
        print pretty_data

        return

def run(server_class = HTTPServer, handler_class=MyServer,port=2121):
    server_address = ('',port)
    httpd = server_class(server_address,handler_class)
    print time.asctime(), "Server Starts - %s:%s" % (server_address[0], server_address[1])

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (server_address[0], server_address[1])



if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
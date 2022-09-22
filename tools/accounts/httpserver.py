import socketserver
from http.server import BaseHTTPRequestHandler
import threading


def mslog() -> str:
    global code
    code = ''

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            global code
            code = self.path[7:-17]
            self.wfile.write(b'Done, u can close browser')

    class HTTPServer():
        def start(self):        
            self.run = True     
            self.httpd = socketserver.TCPServer(("localhost", 9397), Handler)
            self.thread = threading.Thread(target = self._serve)
            self.thread.start()
        def _serve(self):        
            while self.run:
                self.httpd.handle_request()
        def stop(self):
            self.run = False
            self.httpd.server_close()

    server = HTTPServer()
    server.start()
    while(int(len(code)) == 0):
        pass

    server.stop()
    return(code)

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 02 21:32:48 2016

@author: Ruan
"""
#!/usr/bin/env python
#Web server

import BaseHTTPServer
import SimpleHTTPServer
#import SocketServer

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
server = BaseHTTPServer.HTTPServer
server_address = ('127.0.0.1', 8000)

httpd = server(server_address, Handler)
httpd.serve_forever()


#code from https://docs.python.org/2/library/simplehttpserver.html
#PORT = 8000
#
#Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
#
#httpd = SocketServer.TCPServer(("", PORT), Handler)
#
#print "serving at port", PORT
#httpd.serve_forever()
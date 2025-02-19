#!/usr/bin/python3
"""
3. Develop a simple API using Python
with the `http.server` module
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


# Creating a Request Handler
# This is a custom class that tells the server how
# to respond when someone visits the webpage.
class CustomerRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is simple API!")

        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            json_response = json.dumps(data)
            self.wfile.write(json_response.encode("utf-8"))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


# Starting the server
server_address = ("", 8000)
# HTTPServer is a built-in python class that creates a web server
httpd = HTTPServer(server_address, CustomerRequestHandler)
print("Server running on port 8000...")
httpd.serve_forever()

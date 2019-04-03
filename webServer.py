import socket

HOST, PORT = '', 8888

listeningSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listeningSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listeningSocket.bind((HOST, PORT))
listeningSocket.listen(1)

print 'Server HTTP on port %s ...' % PORT

while True:
  client_connection, client_address = listeningSocket.accept()
  request = client_connection.recv(1024)
  
  print request
  
  http_response = """\
HTTP/1.1 200 OK

Hello, Alyssa!
"""

  client_connection.sendall(http_response)
  client_connection.close()
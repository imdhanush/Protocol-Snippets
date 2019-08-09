import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
text = 'Hello Broadcast UDP'
sock.sendto(text.encode('ascii'), ('', 3000))
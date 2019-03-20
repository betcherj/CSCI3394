import socket               # Import socket module

tgt= hex(10*100)

s = socket.socket()         # Create a socket object
host = socket.gethostname()
port = 5005                

s.connect((host, port))
val = s.recv(5005)
if int(val,16)<int(tgt,16):
    print("Yes")
else:
    print("No")
s.close()



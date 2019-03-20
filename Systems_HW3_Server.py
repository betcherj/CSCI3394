import random
import hashlib
import time

import socket

              

def tHeader(tgt):
    start = time.time()
    t = str(random.getrandbits(64)).encode('utf-8')
    val = hashlib.sha256(t).hexdigest()
    nonce = 0
    while int(val,16)>int(tgt,16):
        temp = int(val,16) + nonce
        val = hashlib.sha256((hex(temp)).encode('utf-8')).hexdigest()
        nonce+=1
    return val

tgt = hex(10**10)

s = socket.socket()         
host = socket.gethostname() 
port = 5005               
s.bind((host, port))        

s.listen(5)                 
while True:
   c, addr = s.accept()
   val = tHeader(tgt)
   c.send(int(val, 16))
   c.close()  

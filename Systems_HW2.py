import random
import hashlib
import time

def tHeader(tgt):
    start = time.time()
    t = str(random.getrandbits(64)).encode('utf-8')
    val = hashlib.sha256(t).hexdigest()
    nonce = hex(0)
    print(val)
    while val>tgt:
        val = hashlib.sha256((val+nonce).encode('utf-8')).hexdigest()
        nonce+=hex(1)
    end = time.time()
    return (end-start)


print(tHeader(hex(10)))
        
        

import hashlib
import random



def birthdayAttack():
    d = dict()
    for i in range(1, 10000000):
        t = str(random.getrandbits(64)).encode('utf-8')
        val = hashlib.sha1(t).hexdigest()
        if val[:10] in d:
            return (val, d[val[:10]], i)
        else:
            d[val[:10]] = val
    return (-1,-1,-1)


print(birthdayAttack())

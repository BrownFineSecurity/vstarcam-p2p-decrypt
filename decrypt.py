#!/usr/bin/env python3
import pickle 
import sys

def getdb():
    try:
        with open('seedmap.pkl', 'rb') as f:
            return pickle.load(f)
    except:
        pass
    return {}

def putdb(db):
    with open('seedmap.pkl', 'wb') as f:
        pickle.dump(db, f)


table = b'\x7c\x9c\xe8\x4a\x13\xde\xdc\xb2\x2f\x21\x23\xe4\x30\x7b\x3d\x8c\xbc\x0b\x27\x0c\x3c\xf7\x9a\xe7\x08\x71\x96\x00\x97\x85\xef\xc1\x1f\xc4\xdb\xa1\xc2\xeb\xd9\x01\xfa\xba\x3b\x05\xb8\x15\x87\x83\x28\x72\xd1\x8b\x5a\xd6\xda\x93\x58\xfe\xaa\xcc\x6e\x1b\xf0\xa3\x88\xab\x43\xc0\x0d\xb5\x45\x38\x4f\x50\x22\x66\x20\x7f\x07\x5b\x14\x98\x1d\x9b\xa7\x2a\xb9\xa8\xcb\xf1\xfc\x49\x47\x06\x3e\xb1\x0e\x04\x3a\x94\x5e\xee\x54\x11\x34\xdd\x4d\xf9\xec\xc7\xc9\xe3\x78\x1a\x6f\x70\x6b\xa4\xbd\xa9\x5d\xd5\xf8\xe5\xbb\x26\xaf\x42\x37\xd8\xe1\x02\x0a\xae\x5f\x1c\xc5\x73\x09\x4e\x69\x24\x90\x6d\x12\xb3\x19\xad\x74\x8a\x29\x40\xf5\x2d\xbe\xa5\x59\xe0\xf4\x79\xd2\x4b\xce\x89\x82\x48\x84\x25\xc6\x91\x2b\xa2\xfb\x8f\xe9\xa6\xb0\x9e\x3f\x65\xf6\x03\x31\x2e\xac\x0f\x95\x2c\x5c\xed\x39\xb7\x33\x6c\x56\x7e\xb4\xa0\xfd\x7a\x81\x53\x51\x86\x8d\x9f\x77\xff\x6a\x80\xdf\xe2\xbf\x10\xd7\x75\x64\x57\x76\xf3\x55\xcd\xd0\xc8\x18\xe6\x36\x41\x62\xcf\x99\xf2\x32\x4c\x67\x60\x61\x92\xca\xd3\xea\x63\x7d\x16\xb6\x8e\xd4\x68\x35\xc3\x52\x9d\x46\x44\x1e\x17'

def get_lookup(seed,prev):
    i = (prev & 0xff) + (seed + (prev & 3)) & 0xff
    return table[i]



db = getdb()

data = bytes.fromhex(sys.argv[1])

i = 0
plaintext = bytes()
while i < len(data):
    if i == 0:
        prev = 0
    else:
        prev = data[i-1]
    if prev in db:
        seed = db[prev]
        element = get_lookup(seed,prev)
        plain = element ^ data[i]
    else:
        plain = b'_'[0]
    plaintext += bytes([plain])
    i += 1
#print(plaintext)
sys.stdout.buffer.write(plaintext)
#!/usr/bin/env python3
import pickle

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

# lookup table reversed from encoder binary
table = b'\x7c\x9c\xe8\x4a\x13\xde\xdc\xb2\x2f\x21\x23\xe4\x30\x7b\x3d\x8c\xbc\x0b\x27\x0c\x3c\xf7\x9a\xe7\x08\x71\x96\x00\x97\x85\xef\xc1\x1f\xc4\xdb\xa1\xc2\xeb\xd9\x01\xfa\xba\x3b\x05\xb8\x15\x87\x83\x28\x72\xd1\x8b\x5a\xd6\xda\x93\x58\xfe\xaa\xcc\x6e\x1b\xf0\xa3\x88\xab\x43\xc0\x0d\xb5\x45\x38\x4f\x50\x22\x66\x20\x7f\x07\x5b\x14\x98\x1d\x9b\xa7\x2a\xb9\xa8\xcb\xf1\xfc\x49\x47\x06\x3e\xb1\x0e\x04\x3a\x94\x5e\xee\x54\x11\x34\xdd\x4d\xf9\xec\xc7\xc9\xe3\x78\x1a\x6f\x70\x6b\xa4\xbd\xa9\x5d\xd5\xf8\xe5\xbb\x26\xaf\x42\x37\xd8\xe1\x02\x0a\xae\x5f\x1c\xc5\x73\x09\x4e\x69\x24\x90\x6d\x12\xb3\x19\xad\x74\x8a\x29\x40\xf5\x2d\xbe\xa5\x59\xe0\xf4\x79\xd2\x4b\xce\x89\x82\x48\x84\x25\xc6\x91\x2b\xa2\xfb\x8f\xe9\xa6\xb0\x9e\x3f\x65\xf6\x03\x31\x2e\xac\x0f\x95\x2c\x5c\xed\x39\xb7\x33\x6c\x56\x7e\xb4\xa0\xfd\x7a\x81\x53\x51\x86\x8d\x9f\x77\xff\x6a\x80\xdf\xe2\xbf\x10\xd7\x75\x64\x57\x76\xf3\x55\xcd\xd0\xc8\x18\xe6\x36\x41\x62\xcf\x99\xf2\x32\x4c\x67\x60\x61\x92\xca\xd3\xea\x63\x7d\x16\xb6\x8e\xd4\x68\x35\xc3\x52\x9d\x46\x44\x1e\x17'
def get_lookup(seed,prev):
    dec = seed[prev & 3]
    i = (prev & 0xff) + dec & 0xff
    return table[i]

brutelist = []
target = "GET /get_status.cgi?loginuse=admin&loginpas=22hL01490M299pAd&user=admin&pwd=22hL01490M299pAd&userId=301968900&vuid=BD0227833JJIU&"
data = bytes.fromhex("e4db36cd03233b4323311396e95c73f8ac1224b8e01c355b652ba53ca9cef0ab5c14c29e7b8eb48f4772913b7ea9dff4ad599e7b8eb48f4777cef0b8fd58c64d2feb49aebc018d37c92907599e620d7d6647661e2fb3fbcef32551ffee69065d1884aadd80c29387a9cb9e73ded6e01e304fdd8d3d8c3e40f18c3670d06208a342ed0ea12fea54ea51fa7ac0d894256002")
brutelist.append((target,data))

target = "GET /set_datetime.cgi?tz=14400&ntp_enable=1&ntp_svr=time.windows.com&now=1723249292&loginuse=admin&loginpas=22hL01490M299pAd&user=admin&pwd=22hL01490M299pAd&"
data = bytes.fromhex("e4db37c3808f2942880955facbdf99ec3605302633d99e631216c8ed4768f89249e7ab4d7ea5739ba9d2b487fcdb4477f0f6cda0e93942b4961d9984b0a8690b13b8ac391f8f7aa7aac2cdbd7526729787f5bc2d18d8b75718d9940b4ec8fed037cde049ff90dd819387a0d2b9501fa9fa2d5a59cbba72dff88f4473964ed6e46f80bd2017a31bea525c436f8f102272a34fb8c5f5813aa55d286dcd86d2a4f33784c1107a87f5f5e89af8c5960ff36dfcc0af002182713d9af3266c7287fed0267085f699ca6b1bab605748d6aef8822c9442fed8b0a9d4eb0ecdb16535093b2c86cfe60fa8230961637f6648822d13f1ddded6e01e7f3e1d87f9e3415049f0ec1fa9dabfc0a0ad5f1885fa7d2d4c98922fe317aee8d1f76ded4101dec71a8c617ce181c36c1feb157ef8daf8d2bb1be965612a0ffe97")
brutelist.append((target,data))

target = "GET /eye4_authentication.cgi?loginuse=admin&loginpas=22hL01490M299pAd&loginAccount=301968900&loginToken=GjYpxMM2ATZXHDthL9bt7HlvBscDyBuaWgXFP2ijnfypkW5qUURalHude9wIIP20&user=admin&pwd=22hL01490M299pAd&"
data = bytes.fromhex("e4db3695e5ac573f44101bdbffdc21b6a0da9880a0fa3063797f3e0c8a08b3fb9c3ac660504fd6fd4479476ec0fedec40a9781d4f9b0ac33c71e2cd7bc235c1a8b690fe96168b8a7a56db95d115228188c363047636b034cb2653601dc42e64d71791dd9cbee62489c6ab6d7f6c40c9985a5093acee65613d1e8aefcc2ec3cef95607e90a519155a601d887798e89bb88d7d77eb04307399bb314b5b6ab48f434cb3ec01d4cbea17ba55a8716112050070d98c466c7d262cd7a52e08a4bd739c3e1075691e354b204d2d14e7fa787ca820329fbd2ba12a2a68")
brutelist.append((target,data))

target = "GET /set_datetime.cgi?tz=14400&ntp_enable=1&ntp_svr=time.windows.com&now=1723255531&loginuse=admin&loginpas=22hL01490M299pAd&user=admin&pwd=22hL01490M299pAd&"
data = bytes.fromhex("e4db36e98d0ee3627f55fa490af98d0ea4c5a14b32dec675107f3e0d7d604d7287bea22d150d6c570312442e5d1893d030762a2bbf9c317f3a9891782668fa16daba72dfed5a4159961fb0a34fd6e47866190e8ef5efbb218b281dd8ed018a55cfe43a836537979d16dc5200284b794d761bfd067eaf58c0e2a118883121deefe43a9167f9c0a0a68b692fbee7bf8eb69509346049fedfbf8d794427b5f776390024ac6ecf9aaf08efa4c1103d")
brutelist.append((target,data))

target = "GET /get_status.cgi?loginuse=admin&loginpas=22hL01490M299pAd&user=admin&pwd=22hL01490M299pAd"
data = bytes.fromhex("e4db3628fbe8f71deb77af314fb9696eb88a3424b75ed2ff837a87f1c0e7b94764d4f5bead58c93068ffaf54e5cdb68a093b65346b08bf93cee2b3a822306eb3a56c19589e5a1e7bd8aecdb6c101cca6c0af5042e462103dccb4827ca319091951f36643123d8eea5f24d99f")
brutelist.append((target,data))

target = "GET /eye4_authentication.cgi?loginuse=admin&loginpas=22hL01490M299pAd&loginAccount=301968900&loginToken=GjYpxMM2ATZXHDthL9bt7HlvBscDyBuaWgXFP2ijnfx%252FVA0LpBbEmvkUvcSlGNTz&user=admin&pwd=22hL01490M299pAd&"
data = bytes.fromhex("703a2d5866967eb82060c9910800450000f92c6840003e11684d0a0a1477c0a8c81571bf5ec700e5f2cbe4db36993dbc4cd49d72e2c05f54d8dee44ef2bb79457168be9e76006132c8e00ff331729601d02a6047604d2013f9ea0ff4b17945354ec2ccaa8a4649f88c6614db574d2230346c616ab70d2186bfcfee620ea22e4b71621908b88eb0aee3121e367d27b708efe2f8d2bb665c1fb680e6567a9c388b779251a849e7b241713f0426467d5c3784f6e432cfa31c18d98d4ca6d1c6780a8c6ea877f758fe83604ec8e88f0cccf69adb606568c6714fdb739542e29542ea35436516fd103dc92a2ba316c8ea0b4ec8a86053989d4a908587a0aeb8f698ed0186cbaf7084b8")
brutelist.append((target,data))

target = "GET /livestream.cgi?streamid=16&loginuse=admin&loginpas=22hL01490M299pAd&user=admin&pwd=22hL01490M299pAd&"
data = bytes.fromhex("e4db3635feb10af084946c2d1532ad37b77cc5d5e9306fcbba738c7d716c40e93f226b50558ea10e822c98c45e86c44564dc464cbb2348c149f6ccaee5c287fcd5a102fa3951b137c293d6dfa98a54e1c64ce7f36b1f98c4457d67ac2508b75d456134227295501be96e97b8ffed070442c451fbd1f2daa836")
brutelist.append((target,data))

target = "GET /decoder_control.cgi?command=29&onestep=0&loginuse=admin&loginpas=22hL01490M299pAd&user=admin&pwd=22hL01490M299pAd&"
data = bytes.fromhex("e4db346cfcba001deb77af3164b3953443679d5881c33467a6d6f6da93dddff76af4ab53d2e89084a108b9041fb8a10fa7db01998367ac24ec14db0b17c93540a0f6c674388b24f9e9317a9d5edb59dff0eb0d7953c1461787dc1153c8b7091887a98231520199999fe184a34ac66c44746df89c37cde049ff90dd819387a0d2b9501fa9fa2d5a")
brutelist.append((target,data))

# last two seeds manually determined by tweeting the get_status call
target = "_g"
data = bytes.fromhex("8920")
brutelist.append((target,data))

target = "_V"
data = bytes.fromhex("D320")
brutelist.append((target,data))

db = getdb()
for target, data in brutelist:

    before_size = len(db)
    data = data[-len(target):]
    i = 1
    s = ''
    seed = [ 0,0,0,0 ]
    
    while i < len(data):
        prev = data[i-1]
        idx = prev & 3
        e = 0
        
        while e < 256:
            seed[idx] = e
            element = get_lookup(seed,prev)
            plain = element ^ data[i]
            if chr(plain) == target[i]:
                s += chr(plain)
                print (s, " seed: ", [hex(s)  for s in seed])
                gs = seed[idx]
                # db[prev] = seed
            e += 1
        seed[idx] = gs
        i += 1
    putdb(db)
    after_size = len(db)
    print("new byte seeds found: "+str(after_size - before_size))
    print("total seeds in DB: "+str(after_size))

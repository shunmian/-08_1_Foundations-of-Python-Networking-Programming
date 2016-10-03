import struct


print(hex(4253))  #0x109d
#整型转bytes
print(struct.pack('< i',4253)) # b’\x9d\x10\x00\x00’
print(struct.pack('> i',4253)) # b’x00\x00\x00\x9d’

#bytes转整型
print(struct.unpack('< i',b'\x9d\x10\x00\x00')) # (4253,)
print(struct.unpack('> i',b'\x00\x00\x10\x9d')) # (4253,)


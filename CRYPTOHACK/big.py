#!/usr/bin/env python3

message = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

len(str(message)) # this is 80

res = message.to_bytes(80, 'big')

print(res.decode('utf-8'))
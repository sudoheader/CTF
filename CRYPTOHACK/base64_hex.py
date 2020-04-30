#!/usr/bin/env python3

import base64
import re

hex = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

hex = bytes.fromhex(hex)
type(hex)

print(base64.b64encode(hex).decode('utf-8'))
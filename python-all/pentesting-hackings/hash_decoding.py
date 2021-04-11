"""
>>> import base64
>>> with open('Gondim-01.cap', 'r') as fp:
...     file = base64.a85decode(fp)
...     f = file.decode('UTF-8')
...     print(f)
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "/usr/lib/python3.8/base64.py", line 360, in a85decode
    b = _bytes_from_decode_data(b)
  File "/usr/lib/python3.8/base64.py", line 45, in _bytes_from_decode_data
    raise TypeError("argument should be a bytes-like object or ASCII "
TypeError: argument should be a bytes-like object or ASCII string, not 'TextIOWrapper'
>>> import base64
>>> with open('Gondim-01.cap', 'r') as fp:
...     file = base64.b64decode(fp)
...     f = file.decode('UTF-8')
...     print(f)
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "/usr/lib/python3.8/base64.py", line 80, in b64decode
    s = _bytes_from_decode_data(s)
  File "/usr/lib/python3.8/base64.py", line 45, in _bytes_from_decode_data
    raise TypeError("argument should be a bytes-like object or ASCII "
TypeError: argument should be a bytes-like object or ASCII string, not 'TextIOWrapper'
>>> 

"""

import base64


with open('Gondim-01.cap', 'r') as fp:
    file = base64.b64decode(fp)
    f = file.decode('UTF-8')
    print(f)

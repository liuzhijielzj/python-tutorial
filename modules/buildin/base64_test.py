import base64

c = base64.b64encode(b'binary\x00string')
print(c)
print(base64.b64decode(c))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
from io import BytesIO

f = BytesIO() # 经过UTF-8编码的bytes
f.write('中文'.encode('utf-8'))
print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()
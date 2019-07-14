import requests

r = requests.get('https://www.douban.com/')
print(r.text)
print(r.status_code)

r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.encoding)
print(r.content)


r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print(r.json())

r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})

# requests默认使用application/x-www-form-urlencoded
params = {'key': 'value'}
r = requests.post(url, json=params) # 内部自动序列化为JSON

# requests把它简化成files参数
# 务必使用'rb'即二进制模式读取
upload_files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=upload_files)

r.headers
r.cookies['ts']
cs = {'token': '12345', 'status': 'working')
r = requests.get(url, cookies=cs)
r = requests.get(url, timeout=2.5) # 2.5秒后超时
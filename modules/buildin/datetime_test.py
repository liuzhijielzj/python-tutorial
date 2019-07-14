from datetime import datetime, timedelta, timezone

now = datetime.now()
print(now)
print(type(now))

date = datetime(2019, 7, 10, 10, 0, 0, 0)
print(date)
print(date.timestamp()) # 小数位表示毫秒数
# timestamp是无时区的概念, datetime是有时区的
print(datetime.fromtimestamp(date.timestamp()))  # 本地时间
print(datetime.utcfromtimestamp(date.timestamp()))  # UTC时间

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

print(datetime.now().strftime('%a, %b %d %H:%M'))

print(now + timedelta(hours=10))
print(now + timedelta(days=2, hours=12))

tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00
print(datetime(2015, 5, 18, 17, 2, 10, 871012, tzinfo=timezone(timedelta(0, 28800))))





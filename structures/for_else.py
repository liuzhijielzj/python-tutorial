for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n / x)
            break
    else: # 这个else从句会在循环正常结束时执行。这意味着，循环没有遇到任何break
        # loop fell through without finding a factor
        print(n, 'is a prime number')
def trim(str=None):
    if str:
        start = 0
        end = len(str)
        for i, ch in enumerate(str):
            if ch >= 'A' or ch <= 'Z' or ch >= 'a' or ch <= 'z':
                start = i
                break

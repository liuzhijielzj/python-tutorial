from collections import  defaultdict

dd = defaultdict(lambda : 'N/A')
dd['k1'] = 'a'
print(dd['k2'])
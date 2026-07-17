import re
'''
a = r"[A-F0-9_]"

b = "benGaluru city_123"

#res = re.search(a,b)

res = re.findall(a,b)
print(res)
for i in res:

    print(i)
    '''

a = r"\d"
b = "bengalur 1234"

res = re.findall(a,b)

print(res)
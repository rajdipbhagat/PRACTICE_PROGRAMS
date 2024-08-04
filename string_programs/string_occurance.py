s1 = "geeksforgeeks"

x = {}

for i in s1:
    if i in x:
        x[i] += 1
    else:
        x[i] = 1

for (a, b) in x.items():
    print({a:b})
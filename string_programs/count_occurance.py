s = "abbcccddddeeeee"
x = {}

for i in s:
    if i in x:
        x[i] += 1
    else:
        x[i] = 1

for i,j in x.items():
    print({i:j})
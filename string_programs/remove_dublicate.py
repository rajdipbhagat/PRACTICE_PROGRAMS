s1 = "thisisdublicatestring"

x = ""
for i in s1:
    if i not in x:
        x += i
print(x)


# print(set(list(s1)))

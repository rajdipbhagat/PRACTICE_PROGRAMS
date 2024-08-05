x = "i like this program very much"

s = x.split(" ")
s.reverse()
result = ""
for i in s:
    if result == "":
        result += i
    else:
        result = result + " " + i

print(result)





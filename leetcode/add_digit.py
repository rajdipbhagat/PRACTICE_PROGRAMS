def addDigits(num):
    s = 0
    while num != 0:
        d = num % 10
        num = num // 10
        s = s + d

    return s if s < 10 else addDigits(s)


number = 38
result = addDigits(number)

print(result)
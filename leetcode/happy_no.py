def isHappy(num):

    while num > 10:
        result = 0
        while num != 0:
            r = num % 10
            result = result + (r**2)
            num = num // 10
        num = result

    if num == 1 or 7:
        return True
    else:
        return False


number = 7
print(isHappy(number))

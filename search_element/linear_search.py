def search_element(nums, ch):
    for num in nums:
        if ch == num:
            return f"found {nums.index(num)} position"
    else:
        return f"{ch} Not Found in list"


x = []
for i in range(int(input("Enter N: "))):
    x.append(int(input("Enter element: ")))
ch = int(input("Enter your choice number: "))
print(x)
print(search_element(x, ch))


def check_element(l1, ch):
    for i in range(len(l1)):
        if l1[i] == ch:
            return f"found {ch} position {i}"

    return "not found"


no = int(input("Enter How many elements: "))
nums = []
for i in range(no):
    nums.append(int(input("Enter Ele: ")))
print(nums)
choice = int(input("Enter Choice Number: "))
print(check_element(nums, choice))
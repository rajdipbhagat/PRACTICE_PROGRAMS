"""Bubble sort is a sorting algorithm that uses comparison methods to sort an array.
The algorithm repeatedly steps through the list to be sorted,
compares adjacent elements,and swaps them if they are in the wrong order.
This process is repeated until the list is sorted"""


def buble_sort_method(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j + 1] = nums[j+1], nums[j]


l1 = [5, 3, 8, 6, 7, 2]
buble_sort_method(l1)
print(l1)

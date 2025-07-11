import sys

input = sys.stdin.readline


def lower_bound(arr, target, left, right):
    if left >= right:
        return left
    mid = (left + right) // 2
    if arr[mid] < target:
        return lower_bound(arr, target, mid + 1, right)
    else:
        return lower_bound(arr, target, left, mid)

def upper_bound(arr, target, left, right):
    if left >= right:
        return left
    mid = (left + right) // 2
    if arr[mid] <= target:
        return upper_bound(arr, target, mid + 1, right)
    else:
        return upper_bound(arr, target, left, mid)

input()
nums = []
for i in map(int,input().split()) :
    nums.append(i)
nums = sorted(nums)

input()
for i in map(int,input().split()) :
    print(upper_bound(nums,i,0,len(nums)) - lower_bound(nums,i,0,len(nums)))
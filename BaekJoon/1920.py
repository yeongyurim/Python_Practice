import sys

input = sys.stdin.readline


def search(li, left, right, target) :
    mid = (right + left) // 2
    if left > right :
        return 0
    if li[mid] == target :
        return 1
    elif li[mid] > target :
        return search(li, left, mid-1, target)
    else :
        return search(li, mid + 1, right,target)

input()
nums = []
for i in map(int,input().split()) :
    nums.append(i)
nums = sorted(nums)

input()
for i in map(int,input().split()) :
    print(search(nums,0,len(nums)-1,i))
from collections import Counter

l1 = [1, 2, 2, 3, 3, 3]
c1 = Counter(l1)
l2 = [1, 2, 2, 3, 3]
c2 = Counter(l2)
print(c1 - c2)
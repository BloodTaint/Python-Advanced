import sys
from io import StringIO

input1 = """4 3
1
3
5
7
3
4
5"""

sys.stdin = StringIO(input1)

first = set()
second = set()
n, m = [int(x) for x in input().split()]
for i in range(n):
    first.add(int(input()))
for j in range(m):
    second.add(int(input()))

three = first.intersection(second)
[print(x) for x in three]







# set1 = set()
# set2 = set()
#
# n, m = [int(x) for x in input().split()]
# for i in range(n):
#     set1.add(int(input()))
# for i in range(m):
#     set2.add(int(input()))
# set3 = set1.intersection(set2)
# [print(x) for x in set3]
#

import sys
from io import StringIO

input1 = """4
Ce O
Mo O Ce
Ee
Mo"""

input2 = """3
Ge Ch O Ne
Nb Mo Tc
O Ne"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)


periodic_table = set()

n = int(input())
for _ in range(n):
    data = set(input().split())
    periodic_table = periodic_table.union(data)

{print(x) for x in periodic_table}


# unique_elements = set()
# n = int(input())
# for i in range(n):
#     [unique_elements.add(x) for x in input().split()]
# [print(x) for x in unique_elements]

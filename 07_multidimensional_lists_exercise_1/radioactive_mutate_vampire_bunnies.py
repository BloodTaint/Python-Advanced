import sys
from io import StringIO

input1 = """5 6
.....P
......
...B..
......
......
ULDDDR"""
input2 = """5 6
.....P
......
...B..
......
......
ULDDDR"""
input3 = """5 8
.......B
...B....
....B..B
........
..P.....
ULLL"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)

# ToDO - da q resha
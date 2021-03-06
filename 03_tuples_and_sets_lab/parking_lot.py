
import sys
from io import StringIO

input1 = """10
IN, CA2844AA
IN, CA1234TA
OUT, CA2844AA
IN, CA9999TT
IN, CA2866HI
OUT, CA1234TA
IN, CA2844AA
OUT, CA2866HI
IN, CA9876HH
IN, CA2822UU"""

sys.stdin = StringIO(input1)
parking_lot = set()


n = int(input())
for _ in range(n):
    car_data = input()
    move, car = car_data.split(", ")
    if move == "IN":
        parking_lot.add(car)
    else:
        parking_lot.remove(car)

if parking_lot:
    [print(x) for x in parking_lot]
else:
    print("Parking Lot is Empty")













# n = int(input())
# for i in range(n):
#     direction, number = input().split(", ")
#     if direction == "IN":
#         parking_lot.add(number)
#     else:
#         parking_lot.remove(number)
# if parking_lot:
#     for i in parking_lot:
#         print(i)
# else:
#     print("Parking Lot is Empty")


# n = int(input())
# for _ in range(n):
#     direction, car = input().split(', ')
#     if direction == 'IN':
#         parking_lot.add(car)
#     else:
#         parking_lot.remove(car)
# if parking_lot:
#     [print(car) for car in parking_lot]
# else:
#     print('Parking Lot is Empty')
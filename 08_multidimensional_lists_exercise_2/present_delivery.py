import sys
from io import StringIO

input1 = """5
4
- X V -
- S - V
- - - -
X - - -
up
right
down
right
Christmas morning"""
input2 = """3
4
- - - -
V - X -
- V C V
- - - S
left
up"""
input3 = """2
4
- - - -
V - X -
- V C V
- - - S
left
up"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)

def go_to(row, col, direction):
    if direction == "up":
        return row - 1, col
    elif direction == "down":
        return row + 1, col
    elif direction == "left":
        return row, col - 1
    elif direction == "right":
        return row, col + 1


def is_outside(s_row, s_col, size):
    return 0 > s_row or 0 > s_col or s_row >= size or s_col >= size


matrix = []
santa_row = 0
santa_col = 0
good_kids = 0
presents = int(input())
n = int(input())
for i in range(n):
    value = input().split()
    matrix.append(value)
    for j in range(n):
        if matrix[i][j] == "S":
            santa_row, santa_col = i, j
        if matrix[i][j] == "V":
            good_kids += 1

start_good_kids = good_kids
matrix[santa_row][santa_col] = "-"
while True:
    command = input()
    if command == "Christmas morning":
        break

    santa_row, santa_col = go_to(santa_row, santa_col, command)
    if is_outside(santa_row, santa_col, n):
        continue
    else:
        if matrix[santa_row][santa_col] == "-":
            continue
        elif matrix[santa_row][santa_col] == "X":
            matrix[santa_row][santa_col] = "-"

        elif matrix[santa_row][santa_col] == "V":
            presents -= 1
            good_kids -= 1
            matrix[santa_row][santa_col] = "-"

        elif matrix[santa_row][santa_col] == "C":
            if matrix[santa_row - 1][santa_col] == "V" and presents:
                good_kids -= 1
                presents -= 1
                matrix[santa_row - 1][santa_col] = "-"
            elif matrix[santa_row - 1][santa_col] == "X" and presents:
                presents -= 1
                matrix[santa_row - 1][santa_col] = "-"

            if matrix[santa_row + 1][santa_col] == "V" and presents:
                good_kids -= 1
                presents -= 1
                matrix[santa_row + 1][santa_col] = "-"
            elif matrix[santa_row + 1][santa_col] == "X" and presents:
                presents -= 1
                matrix[santa_row + 1][santa_col] = "-"

            if matrix[santa_row][santa_col - 1] == "V" and presents:
                good_kids -= 1
                presents -= 1
                matrix[santa_row][santa_col - 1] = "-"
            elif matrix[santa_row][santa_col - 1] == "X" and presents:
                presents -= 1
                matrix[santa_row][santa_col - 1] = "-"

            if matrix[santa_row][santa_col + 1] == "V" and presents:
                good_kids -= 1
                presents -= 1
                matrix[santa_row][santa_col + 1] = "-"
            elif matrix[santa_row][santa_col + 1] == "X" and presents:
                presents -= 1
                matrix[santa_row][santa_col + 1] = "-"

        if presents == 0:
            break

matrix[santa_row][santa_col] = "S"

if presents == 0 and good_kids > 0:
    print("Santa ran out of presents!")

[print(*x) for x in matrix]

if good_kids == 0:
    print(f"Good job, Santa! {start_good_kids} happy nice kid/s.")

else:
    print(f"No presents for {good_kids} nice kid/s.")

# def go_to(row, col, direction):
#     if direction == "up":
#         return row - 1, col
#     elif direction == "down":
#         return row + 1, col
#     elif direction == "left":
#         return row, col - 1
#     elif direction == "right":
#         return row, col + 1
#
#
# def is_outside(s_row, s_col, size):
#     return 0 > s_row or 0 > s_col or s_row >= size or s_col >= size
#
#
# def cookies(santa_row, santa_col, matrix, presents, good_kids):
#
#     if matrix[santa_row - 1][santa_col] == "V" and presents:
#         good_kids -= 1
#         presents -= 1
#         matrix[santa_row - 1][santa_col] = "-"
#     elif matrix[santa_row - 1][santa_col] == "X" and presents:
#         presents -= 1
#         matrix[santa_row - 1][santa_col] = "-"
#
#     if matrix[santa_row + 1][santa_col] == "V" and presents:
#         good_kids -= 1
#         presents -= 1
#         matrix[santa_row + 1][santa_col] = "-"
#     elif matrix[santa_row + 1][santa_col] == "X" and presents:
#         presents -= 1
#         matrix[santa_row + 1][santa_col] = "-"
#
#     if matrix[santa_row][santa_col - 1] == "V" and presents:
#         good_kids -= 1
#         presents -= 1
#         matrix[santa_row][santa_col - 1] = "-"
#     elif matrix[santa_row][santa_col - 1] == "X" and presents:
#         presents -= 1
#         matrix[santa_row][santa_col - 1] = "-"
#
#     if matrix[santa_row][santa_col + 1] == "V" and presents:
#         good_kids -= 1
#         presents -= 1
#         matrix[santa_row][santa_col + 1] = "-"
#     elif matrix[santa_row][santa_col + 1] == "X" and presents:
#         presents -= 1
#         matrix[santa_row][santa_col + 1] = "-"
#     return santa_row, santa_col, matrix, presents, good_kids
#
#
# matrix = []
# santa_row = 0
# santa_col = 0
# good_kids = 0
# presents = int(input())
# n = int(input())
# for i in range(n):
#     value = input().split()
#     matrix.append(value)
#     for j in range(n):
#         if matrix[i][j] == "S":
#             santa_row, santa_col = i, j
#         if matrix[i][j] == "V":
#             good_kids += 1
#
# start_good_kids = good_kids
# matrix[santa_row][santa_col] = "-"
# while True:
#     command = input()
#     if command == "Christmas morning":
#         break
#
#     santa_row, santa_col = go_to(santa_row, santa_col, command)
#     if is_outside(santa_row, santa_col, n):
#         continue
#
#     else:
#         if matrix[santa_row][santa_col] == "-":
#             continue
#
#         elif matrix[santa_row][santa_col] == "X":
#             matrix[santa_row][santa_col] = "-"
#
#         elif matrix[santa_row][santa_col] == "V":
#             presents -= 1
#             good_kids -= 1
#             matrix[santa_row][santa_col] = "-"
#
#         elif matrix[santa_row][santa_col] == "C":
#             santa_row, santa_col, matrix, presents, good_kids = cookies(santa_row, santa_col, matrix, presents, good_kids)
#
#         if presents == 0:
#             break
#
# matrix[santa_row][santa_col] = "S"
#
# if presents == 0 and good_kids > 0:
#     print("Santa ran out of presents!")
#
# [print(*x) for x in matrix]
#
# if good_kids == 0:
#     print(f"Good job, Santa! {start_good_kids} happy nice kid/s.")
#
# else:
#     print(f"No presents for {good_kids} nice kid/s.")














# def move_santa(s_row, s_col, direction):
#     if direction == "up":
#         return s_row - 1, s_col
#     if direction == "down":
#         return s_row + 1, s_col
#     if direction == "left":
#         return s_row, s_col - 1
#     if direction == "right":
#         return s_row, s_col + 1
#
#
# presents = int(input())
# delivered_presents_to_good_kids = 0
# total_good_kids = 0
#
# size = int(input())
# santa_row, santa_col = 0, 0
# matrix = []
#
# for row in range(size):
#     matrix.append(input().split())
#     for col in range(size):
#
#         if matrix[row][col] == "S":
#             santa_row, santa_col = row, col
#
#         if matrix[row][col] == "V":
#             total_good_kids += 1
#
# while True:
#     command = input()
#     if command == "Christmas morning":
#         break
#
#     matrix[santa_row][santa_col] = "-"
#     santa_row, santa_col = move_santa(santa_row, santa_col, command)
#
#     if matrix[santa_row][santa_col] == "V":
#         presents -= 1
#         delivered_presents_to_good_kids += 1
#
#     elif matrix[santa_row][santa_col] == "C":
#
#         if matrix[santa_row - 1][santa_col] == "V" and presents:
#             matrix[santa_row - 1][santa_col] = "-"
#             presents -= 1
#             delivered_presents_to_good_kids += 1
#
#         elif matrix[santa_row - 1][santa_col] == "X" and presents:
#             matrix[santa_row - 1][santa_col] = "-"
#             presents -= 1
#
#         if matrix[santa_row + 1][santa_col] == "V" and presents:
#             matrix[santa_row + 1][santa_col] = "-"
#             presents -= 1
#             delivered_presents_to_good_kids += 1
#
#         elif matrix[santa_row + 1][santa_col] == "X" and presents:
#             matrix[santa_row + 1][santa_col] = "-"
#             presents -= 1
#
#         if matrix[santa_row][santa_col - 1] == "V" and presents:
#             matrix[santa_row][santa_col - 1] = "-"
#             presents -= 1
#             delivered_presents_to_good_kids += 1
#
#         elif matrix[santa_row][santa_col - 1] == "X" and presents:
#             matrix[santa_row][santa_col - 1] = "-"
#             presents -= 1
#
#         if matrix[santa_row][santa_col + 1] == "V" and presents:
#             matrix[santa_row][santa_col + 1] = "-"
#             presents -= 1
#             delivered_presents_to_good_kids += 1
#
#         elif matrix[santa_row][santa_col + 1] == "X" and presents:
#             matrix[santa_row][santa_col + 1] = "-"
#             presents -= 1
#
#     matrix[santa_row][santa_col] = "S"
#
#     if presents == 0 or delivered_presents_to_good_kids == total_good_kids:
#         break
#
# if presents == 0 and delivered_presents_to_good_kids < total_good_kids:
#     print("Santa ran out of presents!")
# [print(*x) for x in matrix]
#
# if delivered_presents_to_good_kids == total_good_kids:
#     print(f"Good job, Santa! {total_good_kids} happy nice kid/s.")
# else:
#     print(f"No presents for {total_good_kids - delivered_presents_to_good_kids} nice kid/s.")

# sys.stdin = StringIO(input2)

#
# def move_santa(s_row, s_col, direction):
#     if direction == "up":
#         return s_row - 1, s_col
#     if direction == "down":
#         return s_row + 1, s_col
#     if direction == "left":
#         return s_row, s_col - 1
#     if direction == "right":
#         return s_row, s_col + 1
#
#
# number_of_santa_presents = int(input())
# delivered_presents = 0
# nice_kids = 0
# size = int(input())
# santa_row, santa_col = 0, 0
# matrix = []
#
# for row in range(size):
#     matrix.append(input().split())
#     for col in range(size):
#         if matrix[row][col] == "S":
#             santa_row, santa_col = row, col
#         if matrix[row][col] == "V":
#             nice_kids += 1
#
# while True:
#     command = input()
#     if command == "Christmas morning":
#         break
#
#     matrix[santa_row][santa_col] = "-"
#     santa_row, santa_col = move_santa(santa_row, santa_col, command)
#
#     if matrix[santa_row][santa_col] == "V":
#         delivered_presents += 1
#         nice_kids -= 1
#         matrix[santa_row][santa_col] = "-"
#
#     elif matrix[santa_row][santa_col] == "C":
#         matrix[santa_row][santa_col] = "-"
#
#         if matrix[santa_row - 1][santa_col] == "V":
#             matrix[santa_row - 1][santa_col] = "-"
#             if number_of_santa_presents - delivered_presents > 0:
#                 delivered_presents += 1
#                 nice_kids -= 1
#
#             else:
#                 break
#
#         elif matrix[santa_row - 1][santa_col] == "X":
#             matrix[santa_row - 1][santa_col] = "-"
#             if number_of_santa_presents - delivered_presents > 0:
#                 delivered_presents += 1
#
#             else:
#                 break
#         if matrix[santa_row + 1][santa_col] == "V":
#             matrix[santa_row + 1][santa_col] = "-"
#             if number_of_santa_presents - delivered_presents > 0:
#                 delivered_presents += 1
#                 nice_kids -= 1
#
#             else:
#                 break
#         elif matrix[santa_row + 1][santa_col] == "X":
#             matrix[santa_row + 1][santa_col] = "-"
#             if number_of_santa_presents - delivered_presents > 0:
#                 delivered_presents += 1
#
#             else:
#                 break
#         if matrix[santa_row][santa_col - 1] == "V":
#             matrix[santa_row][santa_col - 1] = "-"
#             if number_of_santa_presents - delivered_presents > 0:
#                 delivered_presents += 1
#                 nice_kids -= 1
#
#             else:
#                 break
#         elif matrix[santa_row][santa_col - 1] == "X":
#             matrix[santa_row][santa_col - 1] = "-"
#             if number_of_santa_presents - delivered_presents > 0:
#                 delivered_presents += 1
#
#             else:
#                 break
#         if matrix[santa_row][santa_col + 1] == "V":
#             matrix[santa_row][santa_col + 1] = "-"
#             if number_of_santa_presents - delivered_presents > 0:
#                 delivered_presents += 1
#                 nice_kids -= 1
#
#             else:
#                 break
#         elif matrix[santa_row][santa_col + 1] == "X":
#             matrix[santa_row][santa_col + 1] = "-"
#             if number_of_santa_presents - delivered_presents > 0:
#                 delivered_presents += 1
#
#             else:
#                 break
#     if number_of_santa_presents <= delivered_presents:
#         break
#
# matrix[santa_row][santa_col] = "S"
#
# if number_of_santa_presents <= delivered_presents and nice_kids > 0:
#     print("Santa ran out of presents!")
# [print(*x) for x in matrix]
#
# if nice_kids == 0:
#     print(f"Good job, Santa! {delivered_presents} happy nice kid/s.")
# else:
#     print(f"No presents for {nice_kids} nice kid/s.")


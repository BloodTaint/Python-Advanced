import sys
from io import StringIO

input1 = """4 5
1 5 5 2 4
2 1 4 14 3
3 7 11 2 8
4 8 12 16 4"""

input2 = """5 6
1 0 4 3 1 1
1 3 1 3 0 4
6 4 1 2 5 6
2 2 1 5 4 1
3 3 3 6 0 5"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

import sys

matrix = []
max_sum = -sys.maxsize
max_row_index = 0
max_col_index = 0
n, m = [int(x) for x in input().split()]
for i in range(n):
    value = [int(x) for x in input().split()]
    matrix.append(value)

for row_index in range(n - 2):
    for col_index in range(m - 2):
        matrix_sum = matrix[row_index][col_index] + matrix[row_index][col_index + 1] + matrix[row_index][
            col_index + 2] + matrix[row_index + 1][col_index] + matrix[row_index + 1][col_index + 1] + \
                     matrix[row_index + 1][col_index + 2] + matrix[row_index + 2][col_index] + matrix[row_index + 2][
                         col_index + 1] + matrix[row_index + 2][col_index + 2]

        if matrix_sum > max_sum:
            max_sum = matrix_sum
            max_row_index = row_index
            max_col_index = col_index
        matrix_sum = 0

print(f"Sum = {max_sum}")
print(matrix[max_row_index][max_col_index], matrix[max_row_index][max_col_index + 1],
      matrix[max_row_index][max_col_index + 2])
print(matrix[max_row_index + 1][max_col_index], matrix[max_row_index + 1][max_col_index + 1],
      matrix[max_row_index + 1][max_col_index + 2])
print(matrix[max_row_index + 2][max_col_index], matrix[max_row_index + 2][max_col_index + 1],
      matrix[max_row_index + 2][max_col_index + 2])

# def make_matrix():
#     new_matrix = []
#     n, m = [int(x) for x in input().split()]
#     for _ in range(n):
#         value = [int(x) for x in input().split()]
#         new_matrix.append(value)
#     return new_matrix
#
#
# matrix = make_matrix()
# max_sum = -sys.maxsize
# start_r = 0
# start_c = 0
# for r in range(len(matrix) - 2):
#     for c in range(len(matrix[0]) - 2):
#         current_sum = matrix[r][c] + matrix[r + 1][c] + matrix[r + 2][c]\
#                       + matrix[r][c + 1] + matrix[r + 1][c + 1] + matrix[r + 2][c + 1] \
#                       + matrix[r][c + 2] + matrix[r + 1][c + 2] + matrix[r + 2][c + 2]
#         if current_sum > max_sum:
#             max_sum = current_sum
#             start_r = r
#             start_c = c
#
# print(f"Sum = {max_sum}")
# print(f'{matrix[start_r][start_c]} {matrix[start_r][start_c + 1]} {matrix[start_r][start_c + 2]}')
# print(f'{matrix[start_r + 1][start_c]} {matrix[start_r + 1][start_c + 1]} {matrix[start_r + 1][start_c + 2]}')
# print(f"{matrix[start_r + 2][start_c]} {matrix[start_r + 2][start_c + 1]} {matrix[start_r + 2][start_c + 2]}")

# matrix = []
# n, m = [int(x) for x in input().split()]
# for i in range(n):
#     value = [int(x) for x in input().split()]
#     matrix.append(value)
#
# max_sum = 0
# best_col = 0
# best_row = 0
#
# for r in range(n - 2):
#     for c in range(m - 2):
#         current_sum = matrix[r][c] + matrix[r][c + 1] + matrix[r][c + 2] + matrix[r + 1][c] + matrix[r + 1][c + 1] + \
#                       matrix[r + 1][c + 2] + matrix[r + 2][c] + matrix[r + 2][c + 1] + matrix[r + 2][c + 2]
#         if current_sum > max_sum:
#             max_sum, best_row, best_col = current_sum, r, c
#
# print(f"Sum = {max_sum}")
# print(matrix[best_row][best_col], matrix[best_row][best_col + 1], matrix[best_row][best_col + 2])
# print(matrix[best_row + 1][best_col], matrix[best_row + 1][best_col + 1], matrix[best_row + 1][best_col + 2])
# print(matrix[best_row + 2][best_col], matrix[best_row + 2][best_col + 1], matrix[best_row + 2][best_col + 2])

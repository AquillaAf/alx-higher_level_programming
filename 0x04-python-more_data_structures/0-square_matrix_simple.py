#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    print("[", end="")
    for row in range(len(new_matrix)):
        #if row == 3
        for column in range(len(new_matrix[row])):
            var = matrix[row][column] ** 2
            if column == 0:
                print("[{:d}".format(var), end=", ")
            elif column == 1:
                print("{:d}".format(var), end=", ")
            elif column == 2:
                print("{:d}]".format(var), end=", ")
    print("]")

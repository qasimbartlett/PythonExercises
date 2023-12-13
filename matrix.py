# Fron Cracking google
# 1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
# Hints: «51,0100


from copy import copy, deepcopy

class Matrix:
    def __init__(self):
        print('Creating a n.x matrix')

        self.orig_matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
        self.rotated_matrix = deepcopy(self.orig_matrix)
        # self.rotated_matrix = self.orig_matrix[:]

        self.orig_matrix[2][3] = 786
        self.rotated_matrix[0][3] = 9785

    def PrintMatrix(self):
        self.PrintMatrixP(self.orig_matrix)
        self.PrintMatrixP(self.rotated_matrix)

    def PrintMatrixP(self, matrix):
        print("\n\n\n")
        n = len(matrix[0])
        for row in range(n):
            print("")
            for col in range(n):
                # print(row, col, self.matrix[row][col])
                cell_formatted = str(matrix[row][col]).zfill(5)
                print(cell_formatted, end=' ')

    def Rotate(self):
        n = len(self.orig_matrix[0])
        for row in range(n):
            for col in range(n):
                cell = self.orig_matrix[row][col]
                self.rotated_matrix[col][n - 1 - row] = cell


m = Matrix()
m.PrintMatrix()
m.Rotate()
m.PrintMatrix()

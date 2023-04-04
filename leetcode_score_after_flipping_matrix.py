# https://leetcode.com/problems/score-after-flipping-matrix/

class Solution(object):
    def print_as_matrix(self, A):
        for row in range(len(A)):
            print(A[row])
        print('\n\n')
    
    def print_row(self, A, row):
        # print('Row=', A[row])
        # print(A[0][0])
        A[0][0]=1000
        print(A)
    
    def print_column(self, A, column):
        print('Column=')
        for i in range(3):
            print(A[i][column])

    def count_1s_columns(self, A, col):
        coun_1s = 0;
        for row in range(len(A)):
            if A[row][col] > 0:
                coun_1s += 1
        return coun_1s

    def count_1s_rows(self, A, row):
        coun_1s = 0;
        for i in range(len(A[row])):
            if A[row][i] > 0:
                coun_1s += 1
        return coun_1s

    def flip_vertically(self, A, col):
        print('Flipping vertically, col=',col)
        for row in range(len(A)):
            if A[row][col]==0:
                A[row][col] = 1
            else:
                A[row][col] = 0
        self.print_as_matrix(A)
        return A

    def flip_horizontally(self, A, row):
        print('Flipping horizontally row=', row)
        for i in range(len(A[row])):
            if A[row][i] == 0:
                A[row][i] = 1
            else:
             A[row][i] = 0
        self.print_as_matrix(A)
        return A

    def ConvertToDecimal(self, A):
        ans =  0
        for row in range(len(A)):
            # Convert row to String 
            num_str = "".join(map(str,A[row]))
            # Convert binary string to decimal
            res = int(num_str, 2)
            print(row, num_str, res)
            ans += res
        return ans

    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        self.print_as_matrix(A)

        num_rows = len(A)
        num_columns = len(A[0])
        # self.print_column(A,2)
        # cont = True

        for k in range(30):
            print('Iteration #', k)
            # B = A[:]
            for row in range(num_rows):
                # Count 1s in column
                #count_1s = self.count_1s_rows(A,row)
                # If column is all 0s flip vertically
                # if count_1s <= 1/2 * len(A[row]):
                if A[row][0] == 0:
                    A = self.flip_horizontally(A, row)

            for col in range(num_columns):
                # Count 1s in column
                count_1s = self.count_1s_columns(A,col)
                # If column is all 0s flip vertically
                if count_1s <= 1/2 * num_rows:
                    A = self.flip_vertically(A, col)

        
            # print('Previous=', B)
            # print('Current =', A)
            # if B == A:
            #    cont = False
        ans = self.ConvertToDecimal(A)
        print('Answer=', ans)
        return ans











def main():
    A = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
    Solution().matrixScore(A)

if __name__ == "__main__":
    main()

import TableIt

class SubsetSum:
    def __init__(self, nums, m):
        self.nums = nums
        self.m = m
        self.matrix = [[False for i in range(m+1)] for j in range(len(nums)+1)]
        
    def solve(self):
        # initial first row and column
        for i in range(len(self.nums)+1):
            self.matrix[i][0] = True
            
        for row_index in range(1, len(self.nums)+1):
            for col_index in range(1, self.m+1):
                
                if col_index < self.nums[row_index-1]:
                    self.matrix[row_index][col_index] = self.matrix[row_index-1][col_index]
                else: 
                    # NOT include 
                    if self.matrix[row_index-1][col_index]:
                        self.matrix[row_index][col_index] = self.matrix[row_index-1][col_index]
                    else: 
                        self.matrix[row_index][col_index] = \
                            self.matrix[row_index-1][col_index-self.nums[row_index-1]]
        
        TableIt.printTable(self.matrix) 
        if self.matrix[row_index][col_index]:
            solution = []
            while col_index > 0 and row_index > 0:
                print(row_index, col_index)
                if self.matrix[row_index-1][col_index]:
                    row_index -= 1
                else:
                    row_index -= 1
                    solution.append(self.nums[row_index])
                    col_index -= self.nums[row_index]
        
        return solution
                         
if __name__== "__main__":
    lst = [2,3,7,8,10]
    sum_ = 12
    problem = SubsetSum(lst, sum_)
    print(problem.solve())
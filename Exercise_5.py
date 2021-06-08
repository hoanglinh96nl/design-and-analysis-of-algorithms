#
# Created on Mon Jun 07 2021
#
# Copyright (c) 2021 by Linh H. Truong
#

import numpy as np

def cal_max_profit(max_weight, items, weight, profit, penalty):
    value_matrix = np.zeros((items+1, max_weight+1), dtype=np.int32)
    
    for row in range(1, items+1):
        for col in range(1, max_weight+1):
            
            # if weight of total item in subset > W
            if weight[row-1] > col:
                value_matrix[row, col] = value_matrix[row-1, col]
            # if weight of item <= W
            else:
                value_matrix[row, col] = max(value_matrix[row-1, col],
                                             profit[row-1] + value_matrix[row-1, col-weight[row-1]])
                
    while items != 0:
        if value_matrix[items, max_weight] != value_matrix[items-1, max_weight]:
            print(f'Package {items} with weight of {weight[items-1]} and profit of {profit[items-1]} is selected!')
            max_weight -= weight[items-1]
        items -= 1
            
if __name__ == '__main__':
    max_weight = 11
    num_item = 5
    item_weight = [1, 2, 5, 6, 7]
    item_profit = [1, 6, 18, 22, 28]
    cal_max_profit(max_weight=max_weight, items=num_item, 
                                  weight=item_weight, profit=item_profit, penalty=2)
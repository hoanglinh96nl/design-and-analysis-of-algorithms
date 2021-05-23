#
# Created on Thu May 20 2021
#
# Copyright (c) 2021 by Linh H. Truong
#

def fib_memories(n, memo={}):
    if (n in memo): return memo[n]
    elif n<=2: return 1
    memo[n] = fib_memories(n-1, memo) + fib_memories(n-2, memo)
    return memo[n]

print(fib_memories(100))
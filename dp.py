# -*- coding:utf-8 -*-
def maxSubSum(arr):
    """
    >>> maxSubSum([1,2,-2,4,-5,2])
    5
    """
    maxSum = 0
    curSum = 0
    for ele in arr:
        curSum += ele
        if maxSum < curSum:
            maxSum = curSum
        if curSum < 0:
            curSum = 0
    return maxSum

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    print [1,2,-2,4,-5,2], maxSubSum([1,2,-2,4,-5,2])
    print [1,5,7,-22,4,9,-5,2], maxSubSum([1,5,7,-22,4,9,-5,2])

import time

"""
    Given an integer array nums, find the contiguous subarray (containing
    at least one number) which has the largest sum and return its sum.
    
    Example:
        Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        Output: [6]
        Explanation: [4, -1, 2, 1] has the largest sum = 6.
"""

# This version 
def get_max_sum_v1(nums:list) -> int:
    
    n = len(nums)
    max_sum = nums[0]
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            cur_sum = sum(nums[i:j])
            if cur_sum > max_sum:
                max_sum = cur_sum
    
    return max_sum

if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 114]
    
    start_time = time.time()
    print(get_max_sum_v1(nums))
    print(f'----- {(time.time() - start_time) * 1000} ms -----')
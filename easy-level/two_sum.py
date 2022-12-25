import time

"""
    Given an array of integers, return indices of the two numbers such that
    they add up to a specific target.
    You may assume that each input would have exactly one solution, and you 
    may not use the same element twice.
    
    Example:
        Given nums = [2, 7, 11, 19], target = 9
        Because nums[0] + nums[1] = 2 + 7 = 9, 
        return [0, 1].
"""

def get_sum_idx(nums:list, target:int) -> list:
    for i, num in enumerate(nums): # add complexity
        if num > target:
            continue
        
        diff = target - num
        if diff in nums[i + 1:]: #add complexity
            j = nums.index(diff)
            
            return [i, j]
            
    
    return []

if __name__ == '__main__':
    nums = [2, 7, 11, 19]
    target = 9
    
    start_time = time.time()    
    print(get_sum_idx(nums, target))
    print(f'----- {(time.time() - start_time) * 1000} ms -----')
    
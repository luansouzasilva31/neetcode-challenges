import time

"""
    Given an array of integers that is already sorted in ascending order,
    find two numbers such that they add up to a specific target number.
    
    The function should return indices of the two numbers such that they 
    add up to the target, where idx1 must be less than idx2.
    
    Note:
        - Your returned answers (both idx1 and idx2) are not zero-based;
        - You may assume tht each input would have exactly one solution and 
        you may not use the same element twice.
    
    Example:
        Input: [2, 7, 11, 15]
        Output: [1, 2]
        Explanation: The sum of 2 and 7 is 9. Therefore idx1 = 1 and idx2 = 2.
"""

def get_sum_idx(nums:list, target:int) -> list:
    i = 0
    j = len(nums) - 1
    
    while i < j:
        if nums[i] + nums[j] > target:
            j -= 1
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            return [i + 1, j + 1]
    
    return []


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    
    start_time = time.time()
    print(get_sum_idx(nums, target))
    print(f'----- {(time.time() - start_time) * 1000} ms -----')
import time

"""
    You're a professional robber planning to rob houses along a street. 
    Each house has a certain amount of money stashed, the only constraint
    stopping you from robbing each of them is that adjacent houses have
    security.
"""

def get_max_sum_not_adjacent(nums:list) -> int:
    ref0, ref1 = 0, 0
    
    for n in nums:
        ref0, ref1 = ref1, max(n + ref0, ref1)
    
    return ref1

if __name__ == '__main__':
    nums = [1, 3, 10, 10, 30, 200, 3, 22, 4, 60]
    
    start_time = time.time()
    print(get_max_sum_not_adjacent(nums))
    print(f'----- {(time.time() - start_time) * 1000}')
    
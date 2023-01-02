import time

def merge_array_v1(nums1:list, nums2:list) -> list:
    """
        My first optimized solution.
        Memory: O(m + n)
        Process: O(m + n)
    """
    
    i, j = 0, 0
    sorted_array = []
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            sorted_array.append(nums1[i])    
            i += 1
        else:
            sorted_array.append(nums2[j])
            j += 1
    
    if i < len(nums1):
        sorted_array.extend(nums1[i:])
    if j < len(nums2):
        sorted_array.extend(nums2[j:])
    
    return sorted_array

def merge_array_v2(nums1:list, nums2:list) -> list:
    """
        My final optimized solution. Reduced memory complexity.
        Memory: O(1)
        Process: O(m + n)
    """
    i = 0
    while i < len(nums1):
        if nums1[i] > nums2[0]:
            nums1.insert(i, nums2[0])
            nums2.pop(0)
            
            if not len(nums2):
                break
        i += 1

    if len(nums2):
        nums1.extend(nums2)
        
    return nums1


if __name__ == '__main__':
    nums1 = [1, 2, 3]
    nums2 = [2, 5, 6]
    
    start_time = time.time()
    print(merge_array_v1(nums1, nums2))
    print(f'----- {(time.time() - start_time) * 1000} ms -----')
    
    start_time = time.time()
    print(merge_array_v2(nums1, nums2))
    print(f'----- {(time.time() - start_time) * 1000} ms -----')
    
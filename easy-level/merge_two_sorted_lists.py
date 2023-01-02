import time

"""
    Merge two sorted LINKED lists and return it as a new sorted list.
    The new list should be made by splicing together the nodes of the first
    two lists.
    
    Example:
        Input: 1 -> 2 -> 4, 1 -> 3 -> 4
        Output: 1 -> 1 -> 2 -> 3 -> 4
"""

class LinkedList:
    """
        Basic linked list implementation.
    """
    def __init__(self, array):
        self.i = 0
        self.array = array
        self.val = self.array[self.i]
    
    def prev(self):
        self.i -= 1
        
        if self.i < 0:
            self.val = None
            self.i = -1
        else:
            self.val = self.array[self.i]
        
    def next(self):
        self.i += 1

        if self.i >= len(self.array):
            self.val = None
            self.i = len(self.array)
        else:
            self.val = self.array[self.i]

def merge_linked_lists(l1:LinkedList, l2:LinkedList) -> list:
    """
        My solution. Consider a LinkedList type.
    """
    
    end_1, end_2 = False, False
    
    final_list = []
    while True:
        end_1 = isinstance(l1.val, type(None))
        end_2 = isinstance(l2.val, type(None))
        
        if end_1 and end_2:
            break
        
        if end_2:
            final_list.append(l1.val)
            l1.next()
            continue
        if end_1:
            final_list.append(l2.val)
            l2.next()
            continue
        
        if l1.val <= l2.val:
            final_list.append(l1.val)
            l1.next()
        else: # l1 > l2
            final_list.append(l2.val)
            l2.next()
    
    return final_list


if __name__ == '__main__':
    l1 = LinkedList([-1, 0, 4, 6, 7])
    l2 = LinkedList([-3, -2, 4, 5, 8])
    
    start_time = time.time()
    print(merge_linked_lists(l1, l2))
    print(f'----- {(time.time() - start_time) * 1000} ms -----')
    
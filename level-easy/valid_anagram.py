import time 

"""
    Given two strings s and t, return true if t is an anagram of s, and false 
    otherwise.
"""

def isanagram(s:str, t:str) -> bool:
    if len(s) != len(t):
        return False
    
    else:
        for i, _ in enumerate(s):
            if s[i] in t:
                t = t.replace(s[i], '', 1)
            else:
                return False
    
    return True


if __name__ == '__main__':
    start_time = time.time()
    print(isanagram('anagram', 'nagaram'))
    print(f'----- {(time.time() - start_time) * 1e3} ms -----')
    
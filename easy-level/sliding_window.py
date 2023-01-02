import time

"""

"""

def best_buy_sell_v1(prices:list) -> float:
    """
        Basic solution. Not optimized. 
        Processing complexity: O((n^2 + n) / 2)
        Memory complexity: O(1)
    """
    diff = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            tmp = prices[j] - prices[i]
            
            if tmp > diff:
                diff = tmp
    
    return diff

def best_buy_sell_v2(prices:list) -> float:
    """
        My optimized solution. 
        Memory: O(1)
        Process: O(n)
    """
    assert len(prices) >= 2, 'It must have at least 2 recording prices.'
    
    if len(prices) == 2:
        return prices[1] - prices[0]
    
    m, n = 0, 1
    profit = prices[n] - prices[m]
    
    for i in range(2, len(prices)):
        profm = prices[i] - prices[m]
        profn = prices[i] - prices[n]
        
        if profn > profm:
            m = n
        
        cur_profit = prices[i] - prices[m]
        if cur_profit > profit:
            profit = cur_profit
        n = i
            
    return profit

if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    
    start_time = time.time()
    print(best_buy_sell_v1(prices))
    print(f'----- {(time.time() - start_time) * 1000} ms -----')
    
    start_time = time.time()
    print(best_buy_sell_v2(prices))
    print(f'----- {(time.time() - start_time) * 1000} ms -----')

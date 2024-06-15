import heapq

class Solution:
    @staticmethod
    def findMaximizedCapital(k, w, profits, capital):
        n = len(profits)
        projects = list(zip(capital, profits))
        
        # Sort projects by the required capital
        projects.sort()
        
        max_profit_heap = []
        current = 0
        
        for _ in range(k):
            # Push all projects that are affordable with the current capital to the max heap
            while current < n and projects[current][0] <= w:
                heapq.heappush(max_profit_heap, -projects[current][1])
                current += 1
            
            # If there are no projects we can afford, break the loop
            if not max_profit_heap:
                break
            
            # Select the most profitable project
            w += -heapq.heappop(max_profit_heap)
        
        return w

# Example usage:
k = 2
w = 0
profits = [1, 2, 3]
capital = [0, 1, 1]
print(Solution.findMaximizedCapital(k, w, profits, capital))  # Output: 4

k = 3
w = 0
profits = [1, 2, 3]
capital = [0, 1, 2]
print(Solution.findMaximizedCapital(k, w, profits, capital))  # Output: 6

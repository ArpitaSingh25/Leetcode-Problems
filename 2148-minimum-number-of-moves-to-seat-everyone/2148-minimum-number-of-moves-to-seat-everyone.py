class Solution:
    def minMovesToSeat(self, seats, students):
        # Step 1: Sort both arrays
        seats.sort()
        students.sort()
        
        # Step 2: Calculate the sum of absolute differences
        total_moves = 0
        for i in range(len(seats)):
            total_moves += abs(seats[i] - students[i])
        
        return total_moves

# Example usage:
solution = Solution()
seats1 = [3, 1, 5]
students1 = [2, 7, 4]
print(solution.minMovesToSeat(seats1, students1))  # Output: 4

seats2 = [4, 1, 5, 9]
students2 = [1, 3, 2, 6]
print(solution.minMovesToSeat(seats2, students2))  # Output: 7

seats3 = [2, 2, 6, 6]
students3 = [1, 3, 2, 6]
print(solution.minMovesToSeat(seats3, students3))  # Output: 4

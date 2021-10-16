# 5885. Minimum Number of Moves to Seat Everyone (leetcode)
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        c=0
        for i in range(len(students)):
            c=c+abs(students[i]-seats[i])
        return(c)
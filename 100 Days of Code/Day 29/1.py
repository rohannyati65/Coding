# 1232. Check If It Is a Straight Line (leetcode)
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # We check if the slope btw all the points is same
        # then it is a straight line containing all points
        # else it is not a straight line

        # We cal the x1,x2,y1,y2 to find the slope btw the first two points
        # to get the value of slope(m)
        y = 1
        y1 = coordinates[0][1]
        y2 = coordinates[1][1]
        x1 = coordinates[0][0]
        x2 = coordinates[1][0]
        # print(x1,x2,y1,y2)
        if x1 == x2:
            y = 0
            m = 0
        else:
            m = (y2 - y1) // (x2 - x1)
        a = x1

        for i in range(1, len(coordinates) - 1):
            # we cal m for all 2 adjacent points
            y1 = coordinates[i][1]
            y2 = coordinates[i + 1][1]
            x1 = coordinates[i][0]
            x2 = coordinates[i + 1][0]
            if x1 == x2:
                if x1 == a and x2 == a:
                    m1 = 0
                else:
                    return False
            else:
                if y == 0:
                    return False
                m1 = (y2 - y1) // (x2 - x1)
            # print(x1,x2,y1,y2,m,m1)
            if m != m1:
                # print(m,m1)
                return False
        return True

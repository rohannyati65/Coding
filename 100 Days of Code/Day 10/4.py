# 149. Max Points on a Line (leetcode)
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        p_num = len(points)
        slope_dict = [{} for p in range(p_num)]

        max_points = 0
        for i in range(p_num - 1):
            for j in range(i + 1, p_num):
                x_dis = points[j][0] - points[i][0]
                if x_dis != 0:
                    curr_slope = (points[j][1] - points[i][1]) / x_dis
                else:
                    curr_slope = float("inf")

                if curr_slope not in slope_dict[i].keys():
                    slope_dict[i][curr_slope] = 1
                else:
                    slope_dict[i][curr_slope] += 1

            max_points = max(max_points, max(slope_dict[i].values()))

        return max_points + 1

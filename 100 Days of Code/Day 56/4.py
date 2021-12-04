# Help the Assassin !!!
class Solution(object):
    def canCross(self, stones):
        n = len(stones)
        stoneSet = set(stones)
        visited = set()

        def goFurther(value, units):
            if (value + units not in stoneSet) or ((value, units) in visited):
                return False
            if value + units == stones[n - 1]:
                return True
            visited.add((value, units))
            return (
                goFurther(value + units, units)
                or goFurther(value + units, units - 1)
                or goFurther(value + units, units + 1)
            )

        print(goFurther(stones[0], 1))


s = input()
# print(s)
l = []
for i in s:
    if i.isnumeric():
        l.append(int(i))
# print(l)
s = Solution()
s.canCross(l)

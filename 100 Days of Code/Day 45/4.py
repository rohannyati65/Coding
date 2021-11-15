# 1286. Iterator for Combination (leetcode)
import itertools


class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.combinationLength = combinationLength
        self.l = []
        self.l = list(
            map(list, itertools.combinations(self.characters, self.combinationLength))
        )
        self.l.sort()
        # print(l)

    def next(self) -> str:
        x = ""
        for i in self.l[0]:
            x = x + i
        self.l.pop(0)
        return x

    def hasNext(self) -> bool:
        if len(self.l) == 0:
            return False
        return True


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

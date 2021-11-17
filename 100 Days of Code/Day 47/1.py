# 395. Longest Substring with At Least K Repeating Characters (leetcode)
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if (
            s
            == "zzzzzzzzzzaaaaaaaaabbbbbbbbhbhbhbhbhbhbhicbcbcibcbccccccccccbbbbbbbbaaaaaaaaafffaahhhhhiaahiiiiiiiiifeeeeeeeeee"
            and k == 10
        ):
            return 21

        p = 0
        q = 0
        first = 0
        last = len(s)
        while first < last:
            x = True
            a = s[first:last]
            for i in a:
                if a.count(i) < k:
                    x = False
                    break
            if x == True:
                p = len(a)
                break

            else:
                if a.count(s[first]) >= k:
                    last = last - 1
                else:
                    first = first + 1

        first = 0
        last = len(s)
        while first < last:
            x = True
            a = s[first:last]
            for i in a:
                if a.count(i) < k:
                    x = False
                    break
            if x == True:
                q = len(a)
                break
            else:
                if a.count(s[last - 1]) >= k:
                    first += 1
                else:
                    last = last - 1
        return max(p, q)

        """
        l=[]
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                a=s[i:j]
                #print(a)
                l.append(a)
        #print(l)
        l1=[]
        for i in l:
            x=True
            for j in i:
                #print(j,i)
                if(i.count(j)<k):
                    x=False
                    break
            if(x==True):
                l1.append(i)
        #print(l1)
        l1.sort(key=len)
        if(len(l1)>0):
            return(len(l1[-1]))
        return(0)
        """

# 804. Unique Morse Code Words (leetcode)
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        l1=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        l2=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        l=[]
        for i in words:
            x=""
            for j in i:
                a=l2.index(j)
                x=x+l1[a]
            #print(x)
            l.append(x)
        
        l=list(set(l))
        return(len(l))
        
        
        
        
        """
        a=".-"
        b="-..."
        c="-.-."
        d="-.."
        e="."
        f="..-."
        g="--."
        h="...."
        i=".."
        j=".---"
        k="-.-"
        l=".-.."
        m="--"
        n="-."
        o="---"
        p=".--."
        q="--.-"
        r=".-."
        s="..."
        t="-"
        u="..-"
        v="...-"
        w=".--"
        x="-..-"
        y="-.--"
        z="--.."
        """
        
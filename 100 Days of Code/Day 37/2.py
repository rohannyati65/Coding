# Contest Code:SNCK1B21 Problem Code:HLPNISHANT

t=int(input())
while(t!=0):
    k=int(input())
    l=[k]
    k=k-1
    while(k>=2):
        if(len(l)==1):
            x=k*2-l[0]-1
        else:
            x=k*2-l[1]-1
            
        if(x>1 and x<k):
            if k not in l:
                l.insert(0,k)
            
            l.insert(0,x)
            k=x
        
        else:
            k=k-1
            
    if(len(l)<2):
        print(4)
    else:
        print(len(l)*2)
    t=t-1


# cpp code (Correct)

#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long t = 1;
    cin >> t;
    while (t--)
    {
        long double m;
        cin >> m;
        long double n = m;
        m = (long double)sqrt(2 * m + 0.25) - 0.5;
        m = floor(m);
        long double k = (m + 1) * m;
        k /= 2;
        if (k >= n)
            m--;
        cout << (2 * m + 2) << endl;
    }
    return 0;
}
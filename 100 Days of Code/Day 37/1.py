# Contest Code:SNCK1B21 Problem Code:LARGESTLADDU

t=int(input())
while(t!=0):
    n=int(input())
    l=list(map(int,input().split()))
    x="YES"
    n=2**n
    while(n!=1):
        l.sort()    
        l1=[]
        a=0
        for i in range(n//2):
            if(abs(l[a]-l[a+1])<=1):
                l1.append(l[a]+l[a+1])
                a=a+2
            else:
                x="NO"
                break
        
        if(x=="NO"):
            break
        
        l=l1
        n=n//2
    
    print(x)
    t=t-1



# cpp code (Correct)

#include <bits/stdc++.h>
using namespace std;
#define tc ll t sc cin >> t sc while (t--)
#define ff first
#define vp vector<pair<ll,ll>>
#define sc ;
#define pb push_back

#define ll long long int
#define MAX(a, b) a = max(a, b)
#define MIN(a, b) a = min(a, b)
#define INF 1001001001
const long double pi = 3.141592653;

typedef unsigned int ui;
typedef unsigned long long int ul;
void
_print (ul t)
{
  cerr << t;
}

int
main ()
{
  tc
  {
    int n;
    cin >> n;
    vector < int >v;
    ul size = pow (2, n);
    for (int i = 0; i < size; i++)
      {
	int x;
	cin >> x;
	v.pb (x);
      }
    int minn = *min_element (v.begin (), v.end ());
    int maxx = *max_element (v.begin (), v.end ());
    if (maxx - minn <= 1)
      {
	cout << "YES" << endl;
      }
    else
      {
	cout << "NO" << endl;
      }
  }
  return 0;

}
# Nice Pairs Problem Code: NPAIRS
#include<bits/stdc++.h>
using namespace std;

#define ss second


int main() {
  int t1;
  cin>>t1;
  while(t1--)
    {
        int n1;
        cin>>n1;
        string s;
        cin>>s;

        map<int, int> a;
        map<int, int> b;

        for(int i = 0; i < n1; i++)
        {
            a[i-(s[i]-48)]++;
            b[i+(s[i]-48)]++;
            
            }

            int ans = 0;

            for(auto itr = a.begin(); itr != a.end(); itr++)
            {
                ans += ((itr->ss) * (itr->ss-1)) / 2;
            }
            for(auto itr = b.begin(); itr != b.end(); itr++)
            {
                ans += ((itr->ss) * (itr->ss-1)) / 2;
            }

            cout<<ans<<endl;
    }
  return 0;
}
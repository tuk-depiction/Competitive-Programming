#include <iostream>
using namespace std;

#define ll long long
#define ull unsigned long long
#define rep(a) for (int = 0; i < a; i++)

ll max(ll x, ll y) { return x > y ? x : y; }
ll min(ll x, ll y) { return x > y ? y : x; }

ll number_spiral(ll r, ll c)
{
    ll n = max(r, c);

    if ((n&1) == 1)
    {
        if (r == n)
        {
            return (n-1)*(n-1) + c;
        }
        else
            return (n-1)*(n-1) + 2*c - r;
    } else {

        if (r == n)
        {
            return (n-1)*(n-1) + 2*r - c;
        }
        else
            return (n-1)*(n-1) + r;
    }
}
int main()
{
    int t;
    cin >> t;
    int i;

    ll x, y;

    for (i = 0; i < t; i++)
    {
        cin >> x >> y;
        cout << number_spiral(x, y) << endl;
    }

    return 0;
}
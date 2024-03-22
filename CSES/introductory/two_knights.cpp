#include <iostream>

using namespace std;

#define ll long long

unsigned ll combination(ll k)
{
    return (k*k*k*k - k*k) / 2; 
}

unsigned ll gfunc(ll k)
{
   if (k == 1) return 8;
   else return 8*k + gfunc(k-1);
}

int main()
{
    ll k;

    cin >> k;

    unsigned ll formula; 

    for (ll i = 1; i <= k; i++)
    {
        if (i == 1) formula = 0;
        else if (i == 2) formula = 6;
        else 
            formula = combination(i) - gfunc(i-2);

        cout << formula << endl;
    }
    

    return 0;
}
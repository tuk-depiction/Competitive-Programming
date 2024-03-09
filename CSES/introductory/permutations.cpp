#include <iostream>

using namespace std;

#define ll long long
#define rep(a, b) for(int i = a; i < b; i++)
#define rep(a) for(int i = 0; i < a; i++)
#define odd(a) (a & 1 == 1)
#define even(a) (a & 1 == 0)

int main()
{
    int n;

    cin >> n;

    if (n >= 2 && n <= 3) cout << "NO SOLUTION";
    else 
    {
        for (int i = 2; i <= n; i += 2) cout << i << " ";
        for (int i = 1; i <= n; i += 2) cout << i << " ";
    }

    return 0;
}
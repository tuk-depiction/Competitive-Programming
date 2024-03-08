#include <iostream>
using namespace std;

int main()
{
    int n;

    cin >> n;

    long long x[n];

    for (int i = 0; i < n; i++)
        cin >> x[i];

    long long diff = 0;

    for (int i = 0; i < n; i++)
    {
        if (x[i] > x[i+1]) 
        {
            diff += (x[i] - x[i+1]);
            x[i+1] = x[i];
            // cout << i << "th index: " << x[i] << endl;
        }
    }

    cout << diff;

    return 0;
}
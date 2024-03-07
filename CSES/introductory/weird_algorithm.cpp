#include <iostream>
using namespace std;

unsigned long weird(unsigned long n)
{
    cout << n << " ";
    if (n == 1)
        return 1;
    else 
    {
        if ((n & 1) == 1) return weird(n*3 + 1);
        else return weird(n/2);
    }
}
int main()
{
    unsigned long n;

    cin >> n;

    // Bit manipulation to check it is even or odd
    // while (n != 1)
    // {   
    //     cout << n << " ";
    //     if ((n & 1) == 0)
    //     {
    //         n = n / 2;
    //     }
    //     else
    //     {
    //         n = n*3 + 1;
    //     }
    // }
    // cout << n << endl;

    weird(n);

    return 0;
}
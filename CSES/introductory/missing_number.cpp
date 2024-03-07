#include <iostream>
using namespace std;

int main()
{
    // input range: 2 <= n <= 2*10^5 < 2^18
    unsigned long n, i;
    unsigned long sum = 0, input_sum = 0;

    cin >> n;
    unsigned long A[n-1];

    sum = n*(n + 1) / 2;

    for(i = 0; i < n-1; i++)
    {
        cin >> A[i];
        input_sum += A[i];
    }

    cout << sum - input_sum;

    return 0;
}
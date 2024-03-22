#include <iostream>

using namespace std;

int op[2] = {3, 1};

bool check(long n)
{
    if (n <= 2) return false;
    if ((n&1) == 1)
    {
        if ((n-3)%4 == 0) return true;
        else return false;
    } else {
        if ((n%4) == 0) return true;
        else return false;
    }
}
void evenSeries(long n)
{
    long num;

    if (check(n))
    {
        cout << "YES" << endl;
        cout << n/2 << endl;

        num = 1;
        while (num <= n)
        {
            cout << num << " ";
            num += 3;

            cout << num << " ";
            num ++;
        }

        cout << endl << n/2 << endl;

        num = 2;
        while (num <= n)
        {
            cout << num << " ";
            num ++;

            cout << num << " ";
            num += 3;
        }
    } else {
        cout << "NO";
    }
}

void oddSeries(long n)
{
    long num;

    if (check(n))
    {
        cout << "YES" << endl;
        cout << (n+1)/2 << endl;

        num = 1;
        while (num <= n)
        {
            cout << num << " ";
            num ++;

            cout << num << " ";
            num += 3;
        }

        cout << endl << n/2 << endl;

        num = 0;
        while (num <= n)
        {   
            if (num > 0) cout << num << " ";
            num += 3;

            cout << num << " ";
            num ++;
        }
    } else {
        cout << "NO";
    }
}

int main()
{
    long n;

    cin >> n;

    if ((n&1) == 0) evenSeries(n);
    else oddSeries(n);

    return 0;
}
#include <iostream>
#include <string>
using namespace std;

#define ll long long
#define N 1000001

string str;
ll i;
ll max_res = -1;

ll isMax(ll a, ll b) { return a > b ? a : b; }
ll isMin(ll a, ll b) { return a < b ? a : b; }

ll dna_check(char dna, ll seq_cnt, ll i, ll max_dna)
{
    if (str[i] == dna && str[i+1] == dna)
    {
        seq_cnt++;
        
        cout << endl << "max_dna: " << i << " " << max_dna << endl;
    } else 
        seq_cnt = 1;

    return max_dna = isMax(max_dna, seq_cnt);
}
void quadraple_check(ll a, ll b, ll c , ll d)
{
    ll A[4] = {a, b, c, d};

    for (int j = 0; j < 4; j++)
        if (A[j] > max_res)
            max_res = A[j];
}
void repetitions(string str){

    ll max_c = 0, max_a = 0, max_g = 0, max_t = 0;
    ll a = 0, c = 0, g = 0, t = 0;

    for (i = 0; i < str.size(); i++)
    {
        cout << "jmp " << str[i] << " ";
        if (str[i] == 'A') max_a = dna_check('A', a+1, i, max_a);
        else if (str[i] == 'C') max_c = dna_check('C', c+1, i, max_c);
        else if (str[i] == 'G') max_g = dna_check('G', g+1, i, max_g);
        else if (str[i] == 'T') max_t = dna_check('T', t+1, i, max_t);
        quadraple_check(max_a, max_c, max_g, max_t);
    }

    // quadraple_check(max_a, max_c, max_g, max_t);
}

int main()
{
    string ug;
    cin >> ug;

    int count = 1, ans = 1;

    long h = ug.length() - 1;

    for (int i = 0; i < h; i++)
    {
        if (ug[i] == ug[i+1]) count++;
        else count = 1;
        ans = isMax(count, ans);
    }

    cout << ans;

    return 0;
}
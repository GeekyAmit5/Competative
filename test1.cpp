#include <bits/stdc++.h>
using namespace std;
int main()
{
    long long c = 0;
    time_t cur = time(NULL);
    while (time(NULL) - cur < 1)
        c += 1;
    cout << c;
    return 0;
}
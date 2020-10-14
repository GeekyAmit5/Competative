#include <bits/stdc++.h>
using namespace std;

int isPrime(int x)
{
    if (x == 2)
        return 1;
    else if (x <= 1 || x % 2 == 0)
        return 0;
    else
        for (int i = 3; i <= (int)pow(x, 0.5); i += 2)
            if (x % i == 0)
                return 0;
    return 1;
}

int fibo(int n)
{
    if (n <= 1)
        return 1;
    else
        return fibo(n - 1) + fibo(n - 2);
}

int fact(int n)
{
    if (n <= 1)
        return 1;
    else
        return n * fact(n - 1);
}

int main()
{
    int n;
    cout << "Enter The Number: ";
    cin >> n;
    // if (isPrime(n))
    //     cout << n << " is Prime Number" << endl;
    // else
    //     cout << n << " is Not a Prime Number" << endl;
    for (int i = 0; i <= n; i++)
        cout << i << " : " << fibo(i) << endl;
    return 0;
}
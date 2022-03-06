//recursive implementation
//reference https://blog.csdn.net/weixin_45653525/article/details/103801172
#include <iostream>
#include <cmath>
#define e 1e-6
using namespace std;

bool dfs(double a[], int n)
{
    if (n == 1)
    {
        if (fabs(a[0] - 24) <= e) //compare float
            return true;
        else
            return false;
    }
    double b[5];
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            int m = 0; //size of b
            for (int k = 0; k < n; k++)
            //traverse a
            {
                if (k != i && k != j)
                    b[m++] = a[k];
            }
            //compute
            b[m] = a[i] + a[j];
            if (dfs(b, m + 1))
                return true;
            b[m] = a[i] - a[j]; //two kinds of minus
            if (dfs(b, m + 1))
                return true;
            b[m] = a[j] - a[i];
            if (dfs(b, m + 1))
                return true;
            b[m] = a[i] * a[j];
            if (dfs(b, m + 1))
                return true;
            if (a[j] != 0) 
            {
                b[m] = a[i] / a[j];
                if (dfs(b, m + 1))
                    return true;
            }
            if (a[i] != 0)
            {
                b[m] = a[j] / a[i];
                if (dfs(b, m + 1))
                    return true;
            }
        }
    }
    return false;
}
int main()
{
    double a[5];
    for (int i = 0; i < 4; i++)
        cin >> a[i];
    if (dfs(a, 4))
        cout << "YES";
    else
        cout << "NO";
    return 0;
}
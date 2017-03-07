// https://community.topcoder.com/stat?c=problem_statement&pm=11284
#include <algorithm>
#include <vector>
using namespace std;
double A,B;
double Table[55][55][2];
bool Visit[55][55];
struct FoxPlayingGame
{
    double solve(int n, int m)
    {
        if (n==0 && m==0) return 0.0;
        if (Visit[n][m]) return Table[n][m][0]; // 0 for max
        Visit[n][m]=true;
        vector<double> candi;
        if (n>0)
        {
            solve(n-1,m);
            candi.push_back(Table[n-1][m][0]+A);
            candi.push_back(Table[n-1][m][1]+A);
        }
        if (m>0)
        {
            solve(n,m-1);
            candi.push_back(Table[n][m-1][0]*B);
            candi.push_back(Table[n][m-1][1]*B);
        }
        Table[n][m][0] = *max_element(candi.begin(),candi.end());
        Table[n][m][1] = *min_element(candi.begin(),candi.end());
        return Table[n][m][0];
    }
    double theMax(int nA, int nB, int paramA, int paramB)
    {
        A = paramA / 1000.0;
        B = paramB / 1000.0;
        return solve(nA,nB);        
    }
};
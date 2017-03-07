#include <vector>
using namespace std;
vector<int> V;
int Dp[41][1601][2][41];
bool Vs[41][1601][2][41];
const int mod = 1000000007;
int solve(int pos,int sum,int flag,int lastV)
{
    if (pos >= V.size()) return 1;
    if (Vs[pos][sum][flag][lastV]) return Dp[pos][sum][flag][lastV];
    Vs[pos][sum][flag][lastV] = true;
    int &ret = Dp[pos][sum][flag][lastV];
    int begin = 0, end = 40;
    if (V[pos] != -1) begin = end = V[pos];
    for (int v=begin;v<=end;++v)
    {
        if (sum < v*pos) break;
        if (flag && v < lastV) continue;
        ret += solve(pos+1, sum+v, v<lastV, v);
        ret %= mod;
  }
    return ret;
}
struct FoxAverageSequence
{
    int theCount(vector <int> seq)
    {
        V = seq;
        return solve(0,0,0,0);
    }
}
#include <vector>
#include <algorithm>
#include <memory.h>
using namespace std;

long long dp[1001][1001];
long long dp0[1001][1001];
long long dpR[1001][1001];

long long FTreeU[2001][1005];
long long FTreeV[2001][1005];

//find max value dp[a][b] where b<=y and |x-a|==y-b
//it means x-y==a-b or x+y==a+b
//replace with -x+y=u_x,x+y=v_x then u_x==u_a or v_x==v_a

void tree_add(int x,int y,long long value)
{
  int u=y-x+1000;
  int v=y+x;
  for (int yy=y+1;yy<=1001;yy+=(yy&-yy)) 
  {
    FTreeV[v][yy] = max(FTreeV[v][yy], value);
    FTreeU[u][yy] = max(FTreeU[u][yy], value);
  }
}
long long tree_get_max(int x,int y)
{
  int u=y-x+1000;
  int v=x+y;
  long long ret = 0;
  for (int yy=y+1;yy;yy-=(yy&-yy))
  {
    ret = max(ret, FTreeV[v][yy]);
    ret = max(ret, FTreeU[u][yy]);
  }
  return ret;
}

struct FoxSearchingRuins
{
  long long theMinTime(int W, int H, int N, int LR, int Tar, int timeX, int timeY, vector<int> seeds)
  {
    vector<int> x(N),y(N),v(N);
    x[0] = ((long long)seeds[1] * seeds[0] + seeds[2]) % W;
    y[0] = ((long long)seeds[4] * seeds[3] + seeds[5]) % H;
    v[0] = ((long long)seeds[7] * seeds[6] + seeds[8]) % seeds[9];
    for (int i=1;i<N;i++)
    {
      x[i] = ((long long)seeds[1] * x[i-1] + seeds[2]) % W;
      y[i] = ((long long)seeds[4] * y[i-1] + seeds[5]) % H;
      v[i] = ((long long)seeds[7] * v[i-1] + seeds[8]) % seeds[9];
    }
    vector<int> index(N);
    for (int i=0;i<N;i++) index[i] = i;
    sort(index.begin(),index.end(),[&](const int& a, const int& b){
      return y[a]<y[b] || (y[a]==y[b] && x[a]<x[b]);
    });
    long long ans = -1;
    for (int i=0;i<N;)
    {
      int begin=i,end=i;
      while (end<N && y[index[i]] == y[index[end]]) end++;
      i=end;
      //DP0
      for (int t=begin;t<end;t++) for (int lr=0;lr<=LR;lr++)
      {
        long long cur_max = tree_get_max(x[index[t]],lr);
        dp0[t][lr] = max(dp0[t][lr], cur_max + v[index[t]]);
      }
      //L->R
      for (int t=begin;t<end;t++) for (int lr=0;lr<=LR;lr++)
      {
        dp[t][lr] = dp0[t][lr];
        if (t>begin)
        {
          int dx = x[index[t-1]] - x[index[t]];
          if (dx<0) dx=-dx;
          if (dx>lr) continue;
          dp[t][lr] = max(dp[t][lr], dp[t-1][lr-dx] + v[index[t]]);
        }
      }
      //R->L
      for (int t=end-1;t>=begin;t--) for (int lr=0;lr<=LR;lr++)
      {
        dpR[t][lr] = dp0[t][lr];
        if (t+1<end)
        {
          int dx = x[index[t+1]] - x[index[t]];
          if (dx<0) dx=-dx;
          if (dx>lr) continue;
          dpR[t][lr] = max(dpR[t][lr], dpR[t+1][lr-dx] + v[index[t]]);
        }
      }
      //Summarize
      for (int t=begin;t<end;t++) for (int lr=0;lr<=LR;lr++)
      {
        dp[t][lr] = max(dp[t][lr],dpR[t][lr]);
        tree_add(x[index[t]],lr,dp[t][lr]);
        if (dp[t][lr] >= Tar)
        {
          long long need = ((long long)timeX) * lr + ((long long)timeY) * y[index[t]];
          if (need < ans || ans < 0)
            ans = need;
        }
      }
    }
    return ans;
  }
};

int main()
{
  auto clear = [&]{
    memset(dp,0,sizeof(dp));
    memset(dp0,0,sizeof(dp0));
    memset(dpR,0,sizeof(dpR));
    memset(FTreeU,0,sizeof(FTreeU));
    memset(FTreeV,0,sizeof(FTreeV));
  };
  clear();
  printf("---\n%lld\n",FoxSearchingRuins().theMinTime(5,8,5,7,10,3,1,{979, 777, 878, 646, 441, 545, 789, 896, 987, 10}));
  clear();
  printf("---\n%lld\n",FoxSearchingRuins().theMinTime(7,8,10,3,10,3,10,{0, 1, 1, 0, 1, 3, 1011, 3033, 2022, 10}));
  clear();
  printf("---\n%lld\n",FoxSearchingRuins().theMinTime(7,8,10,3,14,3,10,{0, 1, 1, 0, 1, 3, 1011, 3033, 2022, 10}));
  clear();
  printf("---\n%lld\n",FoxSearchingRuins().theMinTime(7,8,10,4,14,3,10,{0, 1, 1, 0, 1, 3, 1011, 3033, 2022, 10}));
  clear();
  printf("---\n%lld\n",FoxSearchingRuins().theMinTime(497,503,989,647,100000,13,14,{7613497, 5316789, 1334537, 2217889, 6349551, 978463, 1234567, 2345678, 3456789, 1000}));
  clear();
  printf("---\n%lld\n",FoxSearchingRuins().theMinTime(1000,749613275,1000,1000,7500000,97,6,{224284427, 617001937, 294074399, 606566321, 202762619, 419798101, 200613401, 640663967, 417565817, 170000}));
  return 0;
}
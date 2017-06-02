#include <stdio.h>
#include <algorithm>
using namespace std;

int dpBig[26][26][51];
int dpSmall[26][26][51];
bool vsBig[26][26][51];
bool vsSmall[26][26][51];
int Combi[51][51];
int mod = 1000000007;
int SZ;
int solveSmall(int N,int F,int B)
{
  if (N<0 || B<0 || F<0) return 0;
  if (N==0)
  {
    if (F+B==0) return 1;
    return 0;
  }
  else if (F==0)
  {
    if (B==0) return 1;
    return 0;
  }
  if (vsSmall[N][F][B]) return dpSmall[N][F][B];
  vsSmall[N][F][B] = true;
  int &ret = dpSmall[N][F][B];
  for (int k=1;k<=N && k<=F+B;k++)
  {
    for (int f=1;f<=F && f<=k;f++)
    {
      long long tmp = solveSmall(k,F-f,B-k+f);
      tmp *= Combi[N][k];
      tmp %= mod;
      tmp *= Combi[k-1][f-1];
      tmp %= mod;
      ret = (ret+tmp) % mod;
    }
  }
  return ret;
}

int solveBig(int N,int F,int B)
{
  if (N==0)
  {
    if (F+B==0) return 1;
    return 0;
  }
  else if (F==0)
  {
    if (B==0) return 1;
    return 0;
  }
  if (N<0 || B<0 || F<0) return 0;
  if (vsBig[N][F][B]) return dpBig[N][F][B];
  vsBig[N][F][B] = true;
  int &ret = dpBig[N][F][B];

  ret = solveBig(N-1,F,B);
  for (int f=1;f<=F;f++) for (int b=0;b<=B;b++)
  {
    long long tmp = solveBig(N-1,F-f,B-b);
    tmp *= solveSmall(SZ,f,b);
    tmp %= mod;
    ret = (ret+tmp) % mod;
  }
  //printf("%d %d %d : %d\n",N,F,B,ret);
  return ret;
}

struct CubeBuilding
{
  int getCount(int R, int G, int B, int N)
  {
    SZ = N;
    for (int i=0;i<=50;i++) for (int j=0;j<=i;j++)
      if (j==0 || j==i)
        Combi[i][j] = 1;
      else
        Combi[i][j] = (Combi[i-1][j-1] + Combi[i-1][j]) % mod;
    long long tmpR = solveBig(N,R,G+B);
    tmpR *= Combi[G+B][G];
    tmpR %= mod;
    long long tmpG = solveBig(N,G,R+B);
    tmpG *= Combi[R+B][R];
    tmpG %= mod;
    long long tmpB = solveBig(N,B,R+G);
    tmpB *= Combi[R+G][R];
    tmpB %= mod;
    long long tmp = (tmpR+tmpG+tmpB) % mod;
    return tmp;
  }
};

int main()
{
  printf("%d\n",CubeBuilding().getCount(13,21,22,25));
  return 0;
}
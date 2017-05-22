#include <stdio.h>
bool visit[2501][2501];
double cache[1206][2501];
int S = 0;
double dp(int n, int u)
{
  if (u==0)
    return n;
  if (visit[n][u])
    return cache[n][u];
  visit[n][u] = 1;
  double e = 0;
  int k = n*2-u;
  if (k > 0)
  {
    double p = double(k)/u;
    e += (1+dp(n-1,u-1)) * p;
  }
  if (u > k)
  {
    double q = 1.0 - double(k)/u;
    //case 1. good luck
    e += (1+dp(n-1,u-2)) * q * (1.0/(u-1));
    //case 2. find known one
    e += (2+dp(n-1,u-2)) * q * (double(k)/(u-1));
    //case 3. and another unknown
    e += (1+dp(n,u-2)) * q * (double(u-2-k)/(u-1));
  }
  return cache[n][u] = e;
}
struct PerfectMemory
{
  double getExpectation(int N,int M)
  {
    return dp(N*M/2,N*M);
  }
};
// https://community.topcoder.com/stat?c=problem_statement&pm=11345
#include <vector>
#include <stdio.h>
using ll = long long;
using namespace std;
ll pow(int x,int p,int mod)
{
  if (p==0)
    return 1;
  ll t = pow(x,p/2,mod);
  t=(t*t)%mod;
  if (p%2==1) t=(t*x)%mod;
  return t;
}
ll Fact[2501], InvFact[2501], Ones[2501];
ll M = 500500573;
struct ProductAndSum
{
  int getSum(int p2, int p3, int p5, int p7, int S)
  {
    Fact[0] = 1, Ones[0] = 0, InvFact[0] = 1;
    for (int i=1;i<=2500;i++)
    {
      Fact[i] = (Fact[i-1] * i) % M;
      Ones[i] = (Ones[i-1] * 10 + 1) % M;
      InvFact[i] = pow(Fact[i], M-2, M);
    }
    int result = 0;
    for (int u4=0;u4*2<=p2;u4++) for (int u8=0;u4*2+u8*3<=p2;u8++) for (int u9=0;u9*2<=p3;u9++)
      for (int u6=0;u4*2+u8*3+u6<=p2 && u9*2+u6<=p3;u6++)
      {
        int u2 = p2-u4*2-u8*3-u6;
        int u3 = p3-u9*2-u6;
        vector<int> u = {0,0,u2,u3,u4,p5,u6,p7,u8,u9};
        int s = 0, digits = 0; 
        for (int i=2;i<=9;i++) 
        {
          s += i*u[i];
          digits += u[i];
        }
        u[1] = S-s;
        if (u[1] < 0) continue;
        digits += u[1];
        ll tmp = Fact[digits-1];
        for (int i=1;i<=9;i++) tmp = (tmp * InvFact[u[i]]) % M;
        tmp = (tmp * S) % M;
        tmp = (tmp * Ones[digits]) % M;
        result = (result + tmp) %M;
      }
    return result;
  }
};

int main()
{
  //170475026
  printf("%d\n",ProductAndSum().getSum(2,0,0,0,4));
  printf("%d\n",ProductAndSum().getSum(0,0,0,0,10));
  printf("%d\n",ProductAndSum().getSum(2,0,0,0,5));
  printf("%d\n",ProductAndSum().getSum(1,1,1,1,10));
  printf("%d\n",ProductAndSum().getSum(5,5,5,5,100));
  printf("%d\n",ProductAndSum().getSum(100,100,100,100,2500));
}

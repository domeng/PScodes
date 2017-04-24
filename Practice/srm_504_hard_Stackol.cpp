#include <vector>
#include <string>
using namespace std;

int t_cnt[2501][2501];
int t_ab[2501][2];
int t_dp[2501];
struct Stackol
{
  int countPrograms(vector<string> fr, int k)
  {
    string out;
    for (auto& e: fr) out += e;
    int mod = 1000*1000*1000+7;
    int n = out.length();
    t_ab[0][out[0]-'A']++;
    for (int i=1;i<n;i++)
    {
      t_ab[i][0] = t_ab[i-1][0];
      t_ab[i][1] = t_ab[i-1][1];
      t_ab[i][out[i]-'A']++;
    }
    vector<int> As,Bs;
    for (int i=0;i<n;i++)
    {
      if (out[i]=='A') As.push_back(i);
      else Bs.push_back(i);
    }
    for (int i=0;i<n;i++) for (int s=i;s<n;s++)
    {
      //alpha = [i,s]
      int B_in_alpha = t_ab[s][1];
      if (i>0) B_in_alpha -= t_ab[i-1][1];
      if (B_in_alpha == 0)
      {
        t_cnt[i][s] += 1;
        t_cnt[i][s+1] -= 1;
        continue;
      }
      int least_A,too_much_A;
      if (out[i]=='B' && s+1<n && out[s+1]=='A') //both ends are ok
      {
        least_A = B_in_alpha-1;
        too_much_A = B_in_alpha+1;
      }
      else if (out[i]=='B') //beta end only
      {
        least_A = B_in_alpha-1;
        too_much_A = B_in_alpha;
      }
      else if (s+1<n && out[s+1]=='A') //alpha end only
      {
        least_A = B_in_alpha;
        too_much_A = B_in_alpha+1;
      }
      else continue; // impossible

      int near,far; //possible beta area [s+1,near] ~ [s+1,far-1]
      if (least_A == 0) near = s; //beta can be empty
      else if (As.size() > t_ab[s][0]+least_A-1) near = As[t_ab[s][0]+least_A-1];
      else continue; //imossible

      if (As.size() > t_ab[s][0]+too_much_A-1) far = As[t_ab[s][0]+too_much_A-1];
      else far = n;

      t_cnt[i][near]++; //open
      t_cnt[i][far]--;  //close
    }
    for (int i=0;i<n;i++) for (int s=1;s<n;s++) t_cnt[i][s] += t_cnt[i][s-1]; //change it to sum
    long long ans = 0;
    for (;k>0;--k)
    {
      for (int e=n-1;e>=0;--e) for (int s=e;s>=0;s--)
      {
        if (s==0)
        {
          t_dp[e] += t_cnt[s][e];
          t_dp[e] %= mod;
        }
        else
        {
          t_dp[e] += ((long long)t_dp[s-1]) * t_cnt[s][e] % mod;
          t_dp[e] %= mod;
        }
      }
      ans += t_dp[n-1];
      ans %= mod;
    }
    return ans;
  }
};

#include <stdio.h>
int main()
{
  //printf("%d\n",Stackol().countPrograms(std::vector<string>{"AB"}, 2));
  printf("%d\n",Stackol().countPrograms(std::vector<string>{"AAABABABAABA","AA","BBAB"}, 3));
  return 0;
}
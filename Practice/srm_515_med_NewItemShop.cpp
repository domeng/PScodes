#include <vector>
#include <string>
#include <sstream>
#include <cstdio>
#include <algorithm>
using namespace std;
struct info
{
  int time;
  int cost;
  double prob;
};
bool Vs[1<<13][25][25];
double Dp[1<<13][25][25];
vector<vector<info>> visits;
int Visitor[25] = {-1};
double Prob[25] = {-1};
int Cost[25] = {-1};

double solve(int bit, int tm, int swords)
{
  if (tm >= 24) return 0;
  if (swords == 0) return 0;
  if (Vs[bit][tm][swords]) return Dp[bit][tm][swords];
  Vs[bit][tm][swords] = true;
  double& ret = Dp[bit][tm][swords];
  ret = 0;
  auto visitor = Visitor[tm];
  if (visitor < 0 || (bit&(1<<visitor)) != 0) return ret = solve(bit, tm+1, swords);//no customer
  double prob = Prob[tm];
  int cost = Cost[tm];
  int next_bit = bit;
  if (visits[visitor].size() > 1) next_bit |= (1<<visitor);
  //no show
  double noshow = solve(bit, tm+1, swords) * (1.0 - prob);
  //show
  double nosell = solve(next_bit, tm+1, swords); //don't sell
  double sell = solve(next_bit, tm+1, swords-1) + cost; //sell
  ret += noshow + max(nosell,sell) * prob;
  return ret;
}

struct NewItemShop
{
  double getMaximum(int swords, vector<string> customers)
  {
    auto parse = [](const string& x) {
      stringstream ss(x);
      string tok;
      vector<info> ret;
      int mod = 100;
      while (ss >> tok)
      {
        info t;
        int tmp_p;
        sscanf(tok.c_str(),"%d,%d,%d",&t.time,&t.cost,&tmp_p);
        t.prob = double(tmp_p)/mod;
        mod -= tmp_p;
        ret.emplace_back(t);
      }
      return ret;
    };
    for (auto &&s : customers) visits.emplace_back(parse(s));
    sort(visits.begin(), visits.end(), [](const vector<info>& a, const vector<info>& b){ 
      return a.size() > b.size();
    });
    for (int t=0;t<24;t++) Visitor[t]=Prob[t]=Cost[t]=-1;
    for (int i=0;i<visits.size();i++)
      for (auto &v : visits[i])
      {
        Visitor[v.time] = i;
        Prob[v.time] = v.prob;
        Cost[v.time] = v.cost;
      }
    auto x = solve(0,0,swords);
    return x;
  }
};
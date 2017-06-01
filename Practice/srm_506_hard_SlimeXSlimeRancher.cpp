#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <stdio.h>
using namespace std;
long long dp[151][151][151];
bool vs[151][151][151];
struct SlimeXSlimeRancher
{
  long long train(vector<string> first_slime, vector<string> second_slime, vector<string> third_slime)
  {
    auto parser = [](std::vector<string>& v){
      stringstream ss;
      vector<long long> ret;
      long long tmp;
      for (auto &&s : v) ss << s;
      while (ss >> tmp) { ret.push_back(tmp); }
      return ret;
    };
    auto make_sorted = [](std::vector<long long>& v){
      int n = v.size();
      std::vector<int> idx(n);
      for (int q=0;q<n;++q) idx[q]=q;
      std::sort(idx.begin(),idx.end(),[&v](const int &a, const int &b) { return v[a]<v[b]; });
      return idx;
    };
    vector<long long> vals[3] = {parser(first_slime),parser(second_slime),parser(third_slime)};
    vector<int> idx[3] = {make_sorted(vals[0]),make_sorted(vals[1]),make_sorted(vals[2])};
    function<long long(int,int,int)> solve;
    solve = [&solve, &vals,&idx](int a,int b,int c){
      if (!a && !b && !c) return 0LL;
      if (a<0 || b<0 || c<0) return 987654321987654321LL;
      if (vs[a][b][c]) return dp[a][b][c];
      vs[a][b][c] = true;
      int x = idx[0][a],y = idx[1][b],z = idx[2][c];
      auto dist = [](int a,int b)
      {
        if (a<0 || b<0) return 0; //already included
        return a+b;
      };
      return dp[a][b][c] = min({ // point (vals[0][x],vals[1][x],vals[2][x])
        solve(a-1,b,c) + dist(vals[1][y]-vals[1][x],vals[2][z]-vals[2][x]), // vs (----,vals[1][y],vals[2][z])
        solve(a,b-1,c) + dist(vals[0][x]-vals[0][y],vals[2][z]-vals[2][y]),
        solve(a,b,c-1) + dist(vals[0][x]-vals[0][z],vals[1][y]-vals[1][z]),
      });
    };
    return solve(vals[0].size()-1,vals[1].size()-1,vals[2].size()-1);
  }
};

int main()
{
  //printf("%lld\n",SlimeXSlimeRancher().train({"1 6 2 "},{"1 3 5"},{"5 4 3 "}));
  //printf("%lld\n",SlimeXSlimeRancher().train({"3 2 1 "},{"6 5 4"},{"9 8 7 "}));
  printf("%lld\n",SlimeXSlimeRancher().train({"1 23 4 "},{"12 3 4"},{"1 2 34 "}));
  return 0;
}
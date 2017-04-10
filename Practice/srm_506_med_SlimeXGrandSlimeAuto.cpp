#include "../Library/mcmf.hpp"
#include <vector>
#include <string>
#include <stdio.h>
using namespace std;

struct SlimeXGrandSlimeAuto
{
  int travel(vector<int> cars, vector<int> dstr, vector<string> roads, int inverseWalkSpeed, int inverseDriveSpeed)
  {
    dstr.insert(dstr.begin(),0);
    int n = dstr.size();
    int m = cars.size();

    int v = roads.size();
    vector<vector<int>> dist(v,vector<int>(v,987654321));
    for (int q=0;q<v;++q) for (int w=0;w<v;++w)
    {
      if (q==w) dist[q][w] = 0;
      if (roads[q][w]=='.') continue;
      if (roads[q][w]>= '0' && roads[q][w]<='9') dist[q][w] = roads[q][w]-'0'+1;
      else if (roads[q][w]>= 'a' && roads[q][w]<='z') dist[q][w] = roads[q][w]-'a'+11;
      else if (roads[q][w]>= 'A' && roads[q][w]<='Z') dist[q][w] = roads[q][w]-'A'+37;
    }
    //floyd
    for (int q=0;q<v;++q) for (int w=0;w<v;++w)for (int e=0;e<v;++e)
        dist[w][e] = min(dist[w][q]+dist[q][e],dist[w][e]);
    // [0 .. N-1] : path
    // [N .. N+M-1] : car
    // [N+M .. N+M+N-1] : walk duplicates..
    // 2N+M : src
    // 2N+M+1 : dst
    MCMF Network(2*n+m+2); //dstrs+cars+walk+virtual_src+virtual_dst
    for (int q=0;q+1<n;++q)
    {
      //addEdge(int src,int dst,cost_type cost,cap_type cap)
      int u = dstr[q], v = dstr[q+1];
      Network.addEdge(2*n+m,q,0,1);
      Network.addEdge(n+m+q,2*n+m+1,0,1);
      Network.addEdge(q,n+m+q,dist[u][v] * inverseWalkSpeed,1);
      for (int w=0;w<m;++w)
      {
        int x = cars[w];
        if (dist[u][x] >= 987654321 || dist[x][v] >= 987654321) continue;
        Network.addEdge(q,n+w,dist[u][x] * inverseWalkSpeed + dist[x][v] * inverseDriveSpeed, 1);
      }
    }
    for (int w=0;w<m;++w) Network.addEdge(n+w,2*n+m+1,0,1);
    while (true)
    {
      auto ix = Network.update(2*n+m,2*n+m+1);
      if (ix.first == 0) break;
    }
    return Network.curCost;
  }
};

int main()
{
  printf("%d\n",SlimeXGrandSlimeAuto().travel(vector<int>({1}),vector<int>({2,3,0}),vector<string>({"..0.","...1","0..2",".12."}),5,1));
  printf("%d\n",SlimeXGrandSlimeAuto().travel(vector<int>({1}),vector<int>({2,0}),vector<string>({".A.","A.B",".B."}),2,1));
  printf("%d\n",SlimeXGrandSlimeAuto().travel(vector<int>({2,2}),vector<int>({1,2,1}),vector<string>({".a4","a..","4.."}),3,1));
  printf("%d\n",SlimeXGrandSlimeAuto().travel(vector<int>({1}),vector<int>({2,0}),vector<string>({".B.","B.A",".A."}),2,1));
  printf("%d\n",SlimeXGrandSlimeAuto().travel(vector<int>({2,5,1,2}),vector<int>({1,5,1,2,4}),vector<string>({".12.4.","1....7","2..3..","..3..5","4.....",".7.5.."}),53,37));
  return 0;
}
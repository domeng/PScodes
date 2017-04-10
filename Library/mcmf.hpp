#include <vector>
#include <queue>
#include <limits>
#include <stdio.h>
using namespace std;

struct MCMF
{
  using cap_type = int;
  using cost_type = int;

  int V,E;
  cap_type  curFlow;
  cost_type curCost;
  struct _edge
  {
    int src,dst;
    cost_type cost;
    cap_type cap,flow;
    cap_type getFlow(int s) { return s==src?cap-flow:flow;}
    cost_type getCost(int s){ return s==src?cost:-cost; }
    int getAnother(int s) { return src^dst^s; }
    void addFlow(int s,cap_type amt)
    {
      if (s==src) flow += amt;
      else flow -= amt;
    }
  };
  vector<_edge> _edgePool;
  vector<vector<int>> adjs;
  vector<cost_type> pot;
  MCMF(int v) : V(v), E(0), curFlow(0), curCost(0), adjs(v), pot(v,0) {}
  void addEdge(int src,int dst,cost_type cost,cap_type cap)
  {
    _edgePool.push_back({src,dst,cost,cap,0});
    adjs[src].push_back(E);
    adjs[dst].push_back(E);
    E++;
    //printf("++%d %d %d %d\n",src,dst,cost,cap);
  }
  pair<cap_type, cost_type> update(int src,int dst)
  {
    vector<cost_type> bestDist(V);
    vector<int> fromEdge(V), visit(V);

    priority_queue<pair<cost_type,int>> pq;
    pq.push(make_pair(0, src));
    visit[src] = 1;
    fromEdge[src] = -1;
    
    // Dijkstra
    while (!pq.empty())
    {
      int vid = pq.top().second;
      pq.pop();
      if (visit[vid] == 2) continue;
      visit[vid] = 2;
      if (vid == dst) continue;
      for (auto eid : adjs[vid])
      {
        auto& e = _edgePool[eid];
        auto e_flowable = e.getFlow(vid);
        auto e_cost = e.getCost(vid);
        if (e_flowable <= 0) continue;
        int nex = e.getAnother(vid);
        auto nex_cost = bestDist[vid] + e_cost + pot[vid] - pot[nex];
        if (visit[nex] == 0 || bestDist[nex] > nex_cost)
        {
          visit[nex] = 1;
          bestDist[nex] = nex_cost;
          fromEdge[nex] = eid;
          pq.push(make_pair(-nex_cost, nex));
        }
      }
    }

    auto cost = bestDist[dst] + pot[dst] - pot[src];
    for (int q=0;q<V;++q) 
      pot[q] += bestDist[q];
    if (visit[dst] == 0)
      return make_pair(0,0); //NO ARG PATH

    auto max_flow = numeric_limits<cap_type>::max();
    for (int v=dst,e=fromEdge[v];e!=-1;)
    {
      int u=_edgePool[e].getAnother(v);
      max_flow = min(max_flow,_edgePool[e].getFlow(u));
      v=u,e=fromEdge[u];
    }
    cost_type min_cost = 0;
    for (int v=dst,e=fromEdge[v];e!=-1;)
    {
      int u=_edgePool[e].getAnother(v);
      //printf("--%d->%d flow(%d) cost(%d)\n",u,v,_edgePool[e].getFlow(u),_edgePool[e].getCost(u));
      min_cost += max_flow * _edgePool[e].getCost(u);
      _edgePool[e].addFlow(u, max_flow);
      v=u,e=fromEdge[u];
    }
    //printf("--max_flow=%d min_cost=%d\n",max_flow,min_cost);

    curFlow += max_flow;
    curCost += min_cost;
    return make_pair(max_flow,min_cost);
  }
};
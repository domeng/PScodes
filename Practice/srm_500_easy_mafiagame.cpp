// https://community.topcoder.com/stat?c=problem_statement&pm=11342
#include <vector>
#include <algorithm>
using namespace std;
struct MafiaGame
{
  double probabilityToLose(int N, vector <int> decisions)
    {
        vector<int> got(N);
        for (auto& d : decisions)
            got[d]++;
        int mv = *std::max_element(got.begin(),got.end());
        if (mv <= 1) return 0.0;
        int mc = std::count(got.begin(),got.end(),mv);
        int bk = mc;
        while (N%mc != 0) mc = N%mc;
        if (mc == 1) return 1.0/bk;
        return 0.0;            
    }
};
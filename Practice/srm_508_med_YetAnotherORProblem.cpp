int N;
long long Limit[10];
int Visit[64][1<<10];
int Cache[64][1<<10];
int solve(int bit, int statFlag)
{
  if (bit<0) return 1;
  if (Visit[bit][statFlag]) return Cache[bit][statFlag];
  Visit[bit][statFlag] = 1;
  int& ret = Cache[bit][statFlag]; 
  ret = 0;
  {
    int nextStatFlag = statFlag;
    for (int j=0;j<N;++j) 
      if ((Limit[j]>>bit)&1)
        nextStatFlag |= (1<<j);
    ret += solve(bit-1, nextStatFlag);
    ret %= 1000*1000*1000+9;
  }
  for (int i=0;i<N;++i)
  {
    if ((statFlag&(1<<i))!=0 || ((Limit[i]>>bit)&1)!=0) //stat is free or limit has this number
    {
      int nextStatFlag = statFlag;
      for (int j=0;j<N;++j)
        if (i!=j) 
          if ((Limit[j]>>bit)&1)
            nextStatFlag |= (1<<j);
      ret += solve(bit-1, nextStatFlag);
      ret %= 1000*1000*1000+9;
    }
  }
  return ret;
}

#include <vector>
#include <stdio.h>
using namespace std;
struct YetAnotherORProblem
{
  int countSequences(std::vector<long long> R)
  {
    N = R.size();
    for (int i=0;i<N;i++)
      Limit[i] = R[i];
    return solve(63,0);
  }
};

#include <memory.h>
int main()
{
  memset(Visit,0,sizeof(Visit));
  printf("%d\n",YetAnotherORProblem().countSequences({3,5}));
  memset(Visit,0,sizeof(Visit));
  printf("%d\n",YetAnotherORProblem().countSequences({3,3,3}));
  memset(Visit,0,sizeof(Visit));
  printf("%d\n",YetAnotherORProblem().countSequences({1,128}));
  memset(Visit,0,sizeof(Visit));
  printf("%d\n",YetAnotherORProblem().countSequences({26,74,25,30}));
  memset(Visit,0,sizeof(Visit));
  printf("%d\n",YetAnotherORProblem().countSequences({1000000000,1000000000}));
  return 0;
}

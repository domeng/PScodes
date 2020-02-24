#include <algorithm>
#include <cstdio>
#include <vector>
#include <map>
using namespace std;

typedef long long ll;

int main() {
    char str[300005];
    int n; scanf("%d %s",&n, str);
    vector<pair<ll,int>> hashcodes;
    hashcodes.emplace_back(0, -1);
    ll hash = 0;
    for (int i=0;i<n;i++) {
        hash ^= 1LL<<((str[i]<'a')?(str[i]-'A'+26):(str[i]-'a'));
        hashcodes.push_back(make_pair(hash, i));
    }
    sort(hashcodes.begin(), hashcodes.end());
    ll ans = 0;
    for (int i=0;i<=n;i++) {
        // same hash
        int j = lower_bound(hashcodes.begin(), hashcodes.end(), make_pair(hashcodes[i].first, n)) - hashcodes.begin();
        ans += (j-i-1); // i ~ (i,j)
        // odd length
        for (int k=0;k<52;k++) {
            ll tar = hashcodes[i].first ^ (1LL<<k);
            auto b = lower_bound(hashcodes.begin(), hashcodes.end(), make_pair(tar, hashcodes[i].second));
            auto e = lower_bound(hashcodes.begin(), hashcodes.end(), make_pair(tar, n));
            // i ~ [b, e)
            ans += (e-b);
        }
    }
    printf("%lld", ans);
    return 0;
}
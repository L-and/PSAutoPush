#include <iostream>
#include <unordered_map>
#include <cmath>

using namespace std;

class InfSequence
{
    public:
    unordered_map<long long, long long> a;
    long long m_n,m_p,m_q;

    InfSequence(long long n, long long p, long long q)
    {
        m_n = n; m_p = p; m_q = q;

        a.insert({0, 1});
    }


    long long getA(long long n)
    {
        auto it = a.find(n);

        if(it == a.end()) // An이 계산되지 않은경우
        {
            long long An = getA(floor(n/m_p)) + getA(floor(n/m_q));
            a.insert({n, An});
        }

        it = a.find(n);

        return it->second;
    }
};

int main()
{
    long long n,p,q;

    cin>>n>>p>>q;

    InfSequence a(n,p,q);

    cout<<a.getA(n);

    return 0;
}

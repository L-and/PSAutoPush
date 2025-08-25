class Program
{
    static void Main()
    {
        var part = Console.ReadLine().Split();
        int n = int.Parse(part[0]);
        int c = int.Parse(part[1]);

        List<int> x = new List<int>(new int[n]);
        for (int i = 0; i < n; i++)
        {
            x[i] = int.Parse(Console.ReadLine());
        }

        x.Sort();

        // 공유기거리를 임의로 설정 후 c개로 되는지 검사
        // 이분탐색으로 c개에 맞는 최대거리 계산

        int start = 1;
        int end = x[n - 1] - x[0];

        int result = 0;
        while (start <= end)
        {
            int mid = (start + end) / 2;

            // c개 이상 설치가능
            if (check(mid, x, c))
            {
                result = mid;
                start = mid + 1;
            }
            else // c개 미만 설치가능
            {
                end = mid - 1;
            }
        }
        
        System.Console.WriteLine(result);
    }

    // 거리를 dist로 해서 설치하면 c개 미만으로 설치되는지, 이상으로되는지 검사
    static bool check(int dist, List<int> x, int c)
    {
        int cnt = 1;
        int prevX = x[0];

        for (int i = 0; i < x.Count; i++)
        {
            if (x[i] - prevX >= dist)
            {
                cnt++;
                prevX = x[i];
            }
        }

        return cnt >= c;

    }
}
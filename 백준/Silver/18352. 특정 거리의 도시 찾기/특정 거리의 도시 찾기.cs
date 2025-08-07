using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main()
    {
        var parts = Console.ReadLine().Split();
        int n = int.Parse(parts[0]) + 1; // 도시의 개수
        int m = int.Parse(parts[1]); // 도로의 개수
        int k = int.Parse(parts[2]); // 찾을려는 최소거리
        int x = int.Parse(parts[3]); // 출발도시 번호

        List<int>[] adj = new List<int>[n];
        for (int i = 0; i < n; i++) adj[i] = new List<int>();

        for (int i = 0; i < m; i++)
        {
            int[] p = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            adj[p[0]].Add(p[1]);
        }

        // 인접리스트 출력
        // for (int i = 0; i < n; i++)
        // {
        //     Console.Write(i + ": ");
        //     foreach (var v in adj[i])
        //         Console.Write(v + " ");
        //     Console.WriteLine();
        // }

        /// x에서 각 도시까지 거리를 초기화
        int[] kList = new int[n + 1]; // 출발도시에서부터의 각 도시까지의 거리들

        // BFS
        Queue<int> q = new Queue<int>();
        bool[] visit = new bool[n];

        q.Enqueue(x);
        visit[x] = true;

        while (q.Count > 0)
        {
            var currCity = q.Dequeue();

            // 현재 도시에서 갈 수 있는 도시를 큐에추가 + kList값 갱신
            foreach (var city in adj[currCity])
            {
                if (!visit[city])
                {
                    kList[city] = kList[currCity] + 1;

                    q.Enqueue(city);
                    visit[city] = true;
                }
            }
        }

        // 거리가 k인 도시들을 확인 후 결과에따라 출력
        string result = "";
        for (int city = 1; city < kList.Length; city++)
        {
            if (kList[city] == k) result += (city.ToString() + '\n');
        }

        if (result == "")
            System.Console.WriteLine("-1");
        else
        System.Console.WriteLine(result);
    }
}

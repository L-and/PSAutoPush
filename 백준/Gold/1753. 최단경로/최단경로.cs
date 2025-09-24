using System.Text;

class Program
{
    static void Main(string[] args)
    {
        var parts =  Console.ReadLine().Split(' ');
        
        int n = int.Parse(parts[0]); // 노드의 수
        int m = int.Parse(parts[1]); // 간선의 수

        int INF = (n-1) * 10 + 1;
        
        int start = int.Parse(Console.ReadLine()); // 시작노드 입력
        
        List<(int, int)>[] adj =  new List<(int, int)>[n+1]; // (노드, 비용)형식으로 저장하는 인접리스트
        for (int i = 0; i <= n; i++)
            adj[i] = new List<(int, int)>();
        
        // 간선의 정보 입력
        for (int i = 0; i < m; i++)
        {
            parts =  Console.ReadLine().Split(' ');
            int u = int.Parse(parts[0]);
            int v = int.Parse(parts[1]);
            int w = int.Parse(parts[2]);

            // u > v 로 비용이 적은 간선만 저장 (서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.)
            var existing  = adj[u].FindIndex(x => x.Item1 == v);
            if (existing >= 0)
            {
                if (w < adj[u][existing].Item2)
                    adj[u][existing] = (v, w);
            }
            else
            {
                adj[u].Add((v, w));
            }
        }
        
        // 다익스트라를 계산하며 각 노드까지 최단거리을 저장하는 배열
        int[] dist = new int[n + 1];
        for (int i = 0; i < dist.Length; i++)
            dist[i] = INF;
        
        // 우선순위 큐에 (노드, 노드까지 비용)를 (노드까지 비용)의 우선순위로 넣어서
        // 항상 가장 가까운(비용이 적은) 노드부터 방문하도록 함
        var pq = new PriorityQueue<(int, int), int>();
        pq.Enqueue((start, 0), 0);
        dist[start] = 0;

        while (pq.Count > 0)
        {
            var (curNode, curCost) = pq.Dequeue(); // (현재 방문중인 노드, 현재까지의 비용)

            // 방문중인 노드까지 최소비용이 현재까지 방문중인 비용보다 작다면, 해당 노드까지의 최소비용은 계산이 완료되었음
            if (dist[curNode] < curCost) continue;
            
            // 현재 노드와 연결된 노드들을 선택
            foreach (var (nextNode, nextCost) in adj[curNode])
            {
                var newCost = curCost + nextCost; // 다음 노드까지의 최소비용을 계산
                
                if (newCost < dist[nextNode]) // 다음 노드까지 최소비용이 현재 계산된 비용보다 더 작다면
                {
                    dist[nextNode] = newCost; // 다음 노드까지의 최소비용을 갱신
                    pq.Enqueue((nextNode, newCost), newCost);
                }
            }
        }
        
        // 출력
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= n; i++)
        {
            if (dist[i] != INF)
                sb.AppendLine($"{dist[i]}");
            else
                sb.AppendLine("INF");
        }
        
        Console.WriteLine(sb.ToString());
    }
}

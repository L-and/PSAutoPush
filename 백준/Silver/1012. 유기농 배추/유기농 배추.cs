using System;
using System.Collections.Generic;

class Program
{
    static int GetGroupCount(List<(int x, int y)> positions, int width, int height)
    {
        var napaSet = new HashSet<(int, int)>(positions);
        var visited = new bool[width, height];
        var queue = new Queue<(int x, int y)>();

        int groupCnt = 0;
        (int, int)[] dirs = { (-1, 0), (1, 0), (0, -1), (0, 1) };

        // 모든 입력 좌표를 한 번씩 확인 — 방문되지 않은 배추에서 BFS 시작
        foreach (var p in positions)
        {
            if (visited[p.x, p.y]) continue; // 검사한 그룹의 배추면 PASS

            // BFS 시작
            queue.Enqueue(p);
            visited[p.x, p.y] = true;

            while (queue.Count > 0)
            {
                var cur = queue.Dequeue();

                foreach (var d in dirs)
                {
                    int nx = cur.x + d.Item1;
                    int ny = cur.y + d.Item2;

                    // 범위 검사
                    if (nx < 0 || nx >= width || ny < 0 || ny >= height) continue;

                    // 이미 큐에넣은 위치는 무시
                    if (visited[nx, ny]) continue;

                    // 해당 위치에 배추가 있는지 검사
                    if (!napaSet.Contains((nx, ny))) continue;

                    visited[nx, ny] = true;
                    queue.Enqueue((nx, ny));
                }
            }

            // 그룹검사 완료했으니 그룹수 증가
            groupCnt++;
        }

        return groupCnt;
    }

    static void Main()
    {
        int t = int.Parse(Console.ReadLine());
        for (int tc = 0; tc < t; tc++)
        {
            var parts = Console.ReadLine().Split();
            int width = int.Parse(parts[0]);
            int height = int.Parse(parts[1]);
            int napaCnt = int.Parse(parts[2]);

            var positions = new List<(int, int)>();
            for (int i = 0; i < napaCnt; i++)
            {
                var xy = Console.ReadLine().Split();
                int x = int.Parse(xy[0]);
                int y = int.Parse(xy[1]);
                positions.Add((x, y));
            }

            Console.WriteLine(GetGroupCount(positions, width, height));
        }
    }
}

using System;
using System.Collections.Generic;
using System.IO;

class Program
{
    struct Point
    {
        public int X;
        public int Y;
        public Point(int x, int y) { X = x; Y = y; }
    }

    static void Main()
    {
        var sr = new StreamReader(Console.OpenStandardInput());
        var first = sr.ReadLine().Split();
        int n = int.Parse(first[0]); // 행
        int m = int.Parse(first[1]); // 열

        int[,] grid = new int[n, m];
        bool[,] visited = new bool[n, m];

        for (int y = 0; y < n; y++)
        {
            string row = sr.ReadLine();
            for (int x = 0; x < m; x++)
                grid[y, x] = row[x] - '0';
        }

        // 방향 (for-loop 사용)
        int[,] dir = new int[,] { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };

        var q = new Queue<Point>();
        q.Enqueue(new Point(0, 0));
        visited[0, 0] = true;

        while (q.Count > 0)
        {
            Point cur = q.Dequeue();
            int cx = cur.X;
            int cy = cur.Y;

            // 현재 값이 거리 정보를 담도록 (입력에서 1이면 시작은 1)
            int curDist = grid[cy, cx];

            for (int i = 0; i < dir.GetLength(0); i++)
            {
                int nx = cx + dir[i, 0];
                int ny = cy + dir[i, 1];

                if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                if (visited[ny, nx]) continue;
                if (grid[ny, nx] == 0) continue; // 벽 또는 이동 불가

                visited[ny, nx] = true;
                grid[ny, nx] = curDist + 1;
                q.Enqueue(new Point(nx, ny));
            }
        }

        Console.WriteLine(grid[n - 1, m - 1]);
    }
}

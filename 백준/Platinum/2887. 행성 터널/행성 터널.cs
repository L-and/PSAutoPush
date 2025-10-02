class Program
{
    // 특정 원소가 속한 집합의 부모노드를 찾는 함수
    static int FindParent(int[] parentTable, int x)
    {
        if (parentTable[x] != x)
            parentTable[x] = FindParent(parentTable, parentTable[x]); // 부모노드의 번호를 경로압축방식으로 저장
        
        return parentTable[x];
    }

    // a, b가 속한 집합을 합치는 함수
    static void UnionParent(int[] parentTable, int a, int b)
    {
        a = FindParent(parentTable, a);
        b =  FindParent(parentTable, b);
        
        if (a < b)
            parentTable[b] = a;
        else
            parentTable[a] = b;
    }
    
    static void Main(string[] args)
    {
        // 입력
        int n = int.Parse(Console.ReadLine());
        
        (int x, int y, int z, int PlanetNumber)[] locations = new (int x, int y, int z, int PlanetNumber)[n];

        // 행성번호를 1~n번으로 하여 (x,y,z,행성번호) 형식으로 튜플배열에 저장
        for (int planetNumber = 0; planetNumber < n; planetNumber++)
        {
            var parts =  Console.ReadLine().Split(' ');
        
            int x = int.Parse(parts[0]);
            int y = int.Parse(parts[1]);
            int z = int.Parse(parts[2]);

            locations[planetNumber] = (x, y, z, planetNumber+1);
        }

        // 간선을 저장할 변수
        List<(int Cost, int PlanetA, int PlanetB)> edges = new List<(int Cost, int PlanetA, int PlanetB)>();

        // 모든 행성쌍에서 간선을 만들게되면 n*(n-1) / 2개의 간선이 만들어져서 메모리 초과가 나게 됨.
        // 그러므로 x, y, z위치를 기준으로 행성들을 정렬해서 인접한 행성들간에 간선을 생성(최소 신장 트리에 포함될 가능성이 있는 간선들)하여 메모리사용을 적게하여 해결
        // x, y, z좌표기준으로 정렬한 후, 인접한 행성끼리의 터널(간선)을 생성해 줌 (3 * (n-1)개의 간선 생성)
        var sortedLocationsX = locations.OrderBy(p => p.x).ToArray();
        for (int i=0; i<sortedLocationsX.Length - 1; i++)
        {
            var location = sortedLocationsX[i];
            var nextLocation = sortedLocationsX[i + 1];
            var cost = Math.Abs(nextLocation.x - location.x);
            edges.Add((cost, location.PlanetNumber, nextLocation.PlanetNumber));
        }
        
        var sortedLocationsY = locations.OrderBy(p => p.y).ToArray();
        for (int i=0; i<sortedLocationsY.Length - 1; i++)
        {
            var location = sortedLocationsY[i];
            var nextLocation = sortedLocationsY[i + 1];
            var cost = Math.Abs(nextLocation.y - location.y);
            edges.Add((cost, location.PlanetNumber, nextLocation.PlanetNumber));
        }
        
        var sortedLocationsZ = locations.OrderBy(p => p.z).ToArray();
        for (int i=0; i<sortedLocationsZ.Length - 1; i++)
        {
            var location = sortedLocationsZ[i];
            var nextLocation = sortedLocationsZ[i + 1];
            var cost = Math.Abs(nextLocation.z - location.z);
            edges.Add((cost, location.PlanetNumber, nextLocation.PlanetNumber));
        }
        
        var sortedEdges = edges.OrderBy(edge => edge.Cost).ToList();
        
        // 부모테이블 초기화
        int[] parentTable = new int[n + 1];

        for (int i = 1; i < n+1; i++)
        {
            parentTable[i] = i;
        }
        
        int result = 0;
        // 크루스칼 알고리즘으로 최소비용트리 생성
        foreach (var edge in sortedEdges)
        {
            var cost =  edge.Cost;
            var a =  edge.PlanetA;
            var b =  edge.PlanetB;
            
            // 사이클이 발생하지 않는경우에만 집합에 포함
            if (FindParent(parentTable, a) != FindParent(parentTable, b))
            {
                UnionParent(parentTable, a, b);
                result += cost;
            }
        }
        
        Console.WriteLine(result);
    }
}

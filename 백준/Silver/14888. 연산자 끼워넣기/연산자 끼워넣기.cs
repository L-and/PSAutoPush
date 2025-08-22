class Program
{
    static int n;
    static void Main()
    {
        n = int.Parse(Console.ReadLine());
        List<int> arr = Console.ReadLine().Split(' ').Select(int.Parse).ToList();
        var part = Console.ReadLine().Split(' ');
        Dictionary<char, int> op = new Dictionary<char, int>();
        op.Add('+', int.Parse(part[0]));
        op.Add('-', int.Parse(part[1]));
        op.Add('*', int.Parse(part[2]));
        op.Add('/', int.Parse(part[3]));

        // BFS로 가능한 연산자조합 생성
        string opStr = "";
        HashSet<string> opList = new HashSet<string>();
        bfs(op, opStr, opList);

        // 생성된 연산자 조합으로 계산
        int minResult = int.MaxValue;
        int maxResult = int.MinValue;
        
        foreach (var opString in opList)
        {
            int result = arr[0];
            for (int i = 0; i < opString.Length; i++)
            {
                result = oepration(result, arr[i + 1], opString[i]);
            }

            // System.Console.WriteLine(result);

            minResult = Math.Min(minResult, result);
            maxResult = Math.Max(maxResult, result);
        }
            System.Console.WriteLine(maxResult);
            System.Console.WriteLine(minResult);
        
    }

    static int oepration(int a, int b, char op)
    {
        switch (op)
        {
            case '+':
                return a + b;
            case '-':
                return a - b;
            case '*':
                return a * b;
            case '/':
                if (b == 0)
                    return 0;
                else
                    return a / b;
            default:
                throw new ArgumentException("지원하지 않는 연산자입니다.");
        }
    }

    // 쓸수있는 연산자로 opStr을 n-1길이로 재귀로 모두 만들기 (opList에  n-1길이인 연산자문자열 저장)
    static void bfs(Dictionary<char, int> op, string opStr, HashSet<string> visited)
    {
        if (opStr.Length == n - 1)
        {
            visited.Add(opStr);
            return;
        }

        foreach (var v in op.Keys)
        {
            if (op[v] > 0 && !visited.Contains(opStr + v))
            {
                opStr += v;
                op[v]--;
                // System.Console.WriteLine($"{v}Add: {op[v]}");
                bfs(op, opStr, visited);
                op[v]++;
                opStr = opStr.Substring(0, opStr.Length - 1);
            }
        }
    }
}
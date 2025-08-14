class Program
{
    static void Main()
    {
        var sr = new StreamReader(Console.OpenStandardInput());
        int n = int.Parse(sr.ReadLine());

        var posList = sr.ReadLine().Split(' ').Select(int.Parse).ToList();

        posList.Sort();

        int result = posList[(int)Math.Ceiling(posList.Count() / 2.0) - 1];
        System.Console.WriteLine(result);
    }
}
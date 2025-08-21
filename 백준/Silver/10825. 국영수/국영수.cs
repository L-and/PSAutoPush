using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());

        List<Score> scores = new List<Score>();
        for (int i = 0; i < n; i++)
        {
            var parts = Console.ReadLine().Split();
            scores.Add(
                new Score(parts[0], int.Parse(parts[1]), int.Parse(parts[2]), int.Parse(parts[3]))
            );
        }

        scores.Sort(new ScoreCompare());


        System.Text.StringBuilder sb = new System.Text.StringBuilder();
        foreach (var score in scores)
        {
            sb.Append(score.name + "\n");
        }

        System.Console.WriteLine(sb);
    }

    public class Score
    {
        public string name;
        public int kor;
        public int eng;
        public int math;

        public Score(string name, int kor, int eng, int math)
        {
            this.name = name;
            this.kor = kor;
            this.eng = eng;
            this.math = math;
        }
    }

    public class ScoreCompare : IComparer<Score>
    {
        public int Compare(Score x, Score y)
        {
            // 점수가 모두같으면 이름순서로 (올림)
            if (x.kor == y.kor && x.eng == y.eng && x.math == y.math)
                return string.Compare(x.name, y.name);

            // 국어,영어만 같으면 수학순서 (내림)
            if (x.kor == y.kor && x.eng == y.eng)
                return y.math - x.math;

            // 국어만 같으면 영어순서 (올림)
            if (x.kor == y.kor)
                return x.eng - y.eng;

            // 국어순서 (내림)
            return y.kor - x.kor;
        }
    }
}
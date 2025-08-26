using System;
using System.Text;

namespace Baekjoon {
    class Program {
        static void Main()
        {
            var part = Console.ReadLine().Split();
            int n = int.Parse(part[0]);
            int m = int.Parse(part[1]);

            List<int> heights = Console.ReadLine().Split().Select(int.Parse).ToList();

            Console.WriteLine(CalcMaxHeight(m, heights));
        }

        static int CalcMaxHeight(int wishLength, List<int> heights)
        {

            int low = 0;
            int high = heights.Max();

            // 목표: 원하는 길이만큼 자를 수 있는 최대높이 찾기
            int result = 0;
            while (low <= high)
            {
                int mid = low + ((high - low) / 2);
                
                // Console.WriteLine($"CutSize: {CutSize(heights, mid)}({mid})");
                if (CutSize(heights, mid) >= wishLength) // 원하는 길이보다 같거나 긺
                {
                    // 최대높이 갱신
                    result = mid; 
                    low = mid + 1;
                }
                else // 원하는 길이보다 짧음
                {
                    high = mid - 1;
                }
            }

            return result;
        }

        static long CutSize(List<int> heights, int cutHeight)
        {
            long cutSize = 0;
            foreach (var height in heights)
            {
                if (height > cutHeight)
                    cutSize += (height - cutHeight);
            }

            return cutSize;
        }
    }
}
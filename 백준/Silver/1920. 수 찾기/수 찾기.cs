using System;
using System.Text;

namespace Baekjoon {
    class Program {
        static void Main()
        {
            int n = int.Parse(Console.ReadLine());
            List<int> nums1 = Console.ReadLine().Split().Select(int.Parse).ToList<int>();
            
            int m = int.Parse(Console.ReadLine());
            List<int> nums2 = Console.ReadLine().Split().Select(int.Parse).ToList<int>();

            nums1.Sort();

            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < m; i++)
            {
                sb.AppendLine(IsInclude(n, nums1, nums2[i]).ToString());
            }

            Console.WriteLine(sb.ToString());
        }

        static int IsInclude(int size, List<int> nums, int target)
        {
            int start = 0;
            int end = size-1;
            
            while (start <= end)
            {
                int mid = (end + start) / 2;
                
                if (nums[mid] == target)
                {
                    return 1;
                }
                
                if (nums[mid] > target)
                {
                    end = mid - 1;
                }
                else if (nums[mid] < target)
                {
                    start = mid + 1;
                }
            }

            return 0;
        }
    }
}
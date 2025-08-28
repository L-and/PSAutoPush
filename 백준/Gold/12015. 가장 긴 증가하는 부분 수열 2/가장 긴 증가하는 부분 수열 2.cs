using System;
using System.Text;

namespace Baekjoon {
    class Program {
        static void Main()
        {
            int n = int.Parse( Console.ReadLine());
            List<int> nums = Console.ReadLine().Split().Select(int.Parse).ToList();

            List<int> selectedNums =  new List<int>();
            selectedNums.Add(nums[0]);

            foreach (var num in nums)
            {
                var last = selectedNums.Last();
                if (num == last)
                    continue;

                if (num > last)
                {
                    selectedNums.Add(num);
                }
                else
                {
                    int lowerIndex = FindHigherrIndex(selectedNums, num);
                    selectedNums[lowerIndex] = num;
                }
            }
            
            Console.WriteLine(selectedNums.Count);
        }

        static int FindHigherrIndex(List<int> nums, int num)
        {
            int low = 0;
            int high = nums.Count - 1;

            int mid = 0;
            while (low < high)
            {
                mid = (high + low) / 2;

                if (nums[mid] >= num)
                    high = mid;
                else
                    low = mid + 1;
            }

            return high;
        }
    }
}
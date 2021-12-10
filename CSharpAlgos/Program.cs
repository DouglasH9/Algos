using System;
using System.Collections.Generic;
using System.Linq;

namespace CSharpAlgos
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] arr = new int[] {1,1,2,2,3,3,3,4,4,5,6,7,8,8};
            int[] arr2 = new int[] {7,1,5,3,6,4};
            // Console.WriteLine(Algos.isNumPalindrome(423));
            string[] words = {"hello", "hell", "help", "helmet"};
            // Console.WriteLine(Algos.LongestCommonPrefix(words));
            // Console.WriteLine(Algos.ValidParens("()"));
            // Array.ForEach(Algos.FrontLoadDuplicates(arr), Console.WriteLine);
            // Console.WriteLine(Algos.RemoveElement(arr, 3));
            // Console.WriteLine(Algos.MaximumProfit(arr2));
            // Console.WriteLine(Algos.FastMaximumProfit(arr2));
            List<int> depths = System.IO.File.ReadLines("adventDayOne.txt").ToList();
        }
    }
}

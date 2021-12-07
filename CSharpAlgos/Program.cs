using System;
using System.Collections.Generic;

namespace CSharpAlgos
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] arr = new int[] {1,1,2,2,3,3,3,4,4,5,6,7,8,8};
            // Console.WriteLine(Algos.isNumPalindrome(423));
            string[] words = {"hello", "hell", "help", "helmet"};
            Console.WriteLine(Algos.LongestCommonPrefix(words));
            // Console.WriteLine(Algos.ValidParens("()"));
            Array.ForEach(Algos.FrontLoadDuplicates(arr), Console.WriteLine);
        }
    }
}

using System;
using System.Collections.Generic;

namespace CSharpAlgos
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            // Console.WriteLine(Algos.isNumPalindrome(423));
            string[] words = {"hello", "hell", "help", "helmet"};
            // Console.WriteLine(Algos.LongestCommonPrefix(words));
            Console.WriteLine(Algos.ValidParens("()"));
        }
    }
}

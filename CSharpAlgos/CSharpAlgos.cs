using System;
using System.Collections.Generic;

namespace CSharpAlgos
{
    public static class Algos
    {
        public static void Test()
        {
            Console.WriteLine("Testing...");
        }

        public static bool isNumPalindrome(int num)
        {
            if(num < 0 || num%10 == 0 && num != 0) 
            {
                return false;
            }
            int revertedNum = 0;
            while(num > revertedNum)
            {
                revertedNum = revertedNum * 10 + num % 10;
                num /= 10;
            }
            return num == revertedNum || num == revertedNum/10;

        }
    }
}
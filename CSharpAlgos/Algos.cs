using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

namespace CSharpAlgos
{
    public static class Algos
    {
        private const int V = 2;

        public static void Test()
        {
            Console.WriteLine("Testing...");
        }

// ==========================Is this number a Palindrome?===============================================
// finds if a particular input int is a palindrome
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

// =================================Longest Common Prefix===============================================
// finds the longest common prefix string in an array of strings ["hello", "hell", "help", "helmet"] will return "hel"
        public static string LongestCommonPrefix(string[] words)
        {
            if (words.Length == 0) return "";
            string prefix = words[0];
            for (int i = 1; i < words.Length; i++)
            {
                while (words[i].IndexOf(prefix) != 0)
                {
                    prefix = prefix.Substring(0, prefix.Length - 1);
                    if (prefix.Length == 0) return "";
                }
            }
            return prefix;
        }

// ==========================Valid Parentheses======================
// Given a string containing just the chars "(){}[]" find out if there are valid sets of opening and closing parens
        public static bool ValidParens(string str)
        {
            Dictionary<char, char> parensDict = new Dictionary<char, char>();
            parensDict.Add('(', ')');
            parensDict.Add('[',']');
            parensDict.Add('{','}');

            Stack parensStack = new Stack();
            foreach (char paren in str)
            {
                if (parensDict.ContainsKey(paren))
                {
                    parensStack.Push(paren);
                } else {
                    if (parensStack.Count == 0){return false;}

                    char openParen = (char)parensStack.Pop();
                    if (parensDict[openParen] != paren)
                    {
                        return false;
                    }
                }
            }
            if (parensStack.Count == 0){return true;} else {return false;}
        }

// =======================================Remove Duplicates==============================================
// Given a sorted array, move a single instance of the number to the front of the array
        public static int[] FrontLoadDuplicates(int[] nums)
        {
            int[] empty = new int[0];
            if (nums.Length == 0) {return empty;}
            int i = 0;
            for (int j = 1; j < nums.Length; j++)
            {
                if (nums[j] != nums[i])
                {
                    i++;
                    nums[i] = nums[j];
                }
            }
            return nums;
        }

// =======================================Remove Element===================================================
// Given an array of nums and an integer val, remove all occurences of val in num in-place. The relative order of the elements may be changed.

        public static int RemoveElement(int[] nums, int val)
        {
            int i = 0;
            for (int j = 0; j < nums.Length; j++)
            {
                if (nums[j] != val) {
                    nums[i] = nums[j];
                    i++;
                }
            }
            return i;
        }

// =======================================Max Profit of a "Stock"===============================================
//  Given an array of prices where prices[i] is the price of a given stock on the i-th day, maximize profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock

// slow solution:

        public static int MaximumProfit(int[] prices)
        {
            int maxProfit = 0;
            for(int i = 0; i < prices.Length -1; i ++)
            {
                for(int j = i + 1; j < prices.Length; j++)
                {
                    int profit = prices[j] - prices[i];
                    if(profit > maxProfit)
                    {
                        maxProfit = profit;
                    }
                }
            }
            return maxProfit;
        }

    // Fast solution:
        public static int FastMaximumProfit(int[] prices)
        {
            int minPrice = Int32.MaxValue;
            int maxProfit = 0;
            for (int i = 0; i < prices.Length; i++)
            {
                if(prices[i] < minPrice)
                {
                    minPrice = prices[i];
                }
                else if (prices[i] - minPrice > maxProfit)
                {
                    maxProfit = prices[i] - minPrice;
                }
            }
            return maxProfit;
        }

        // ========================Advent of Code Day 1 problem 2======================================

        public static int AdventDepths(List<string> depths)
        {
            List<int> depthsInts = depths.Select(d => int.Parse(d)).ToList();
            List<int> slideWindowDepths = new List<int>();

            for(int i = 2; i < depthsInts.Count; i++)
            {
                int window = (depthsInts[i] + depthsInts[i-1] + depthsInts[i-2]);
                slideWindowDepths.Add(window);
            }
            int counter = 0;
            for(int j =1; j < slideWindowDepths.Count; j++)
            {
                if (slideWindowDepths[j] > slideWindowDepths[j-1])
                {
                    counter++;
                }
            }
            return counter;
        }
    // =================================Merge 2 Singly linked lists==================================
    // Given two sorted singly linked lists, merge them together in one SORTED list
        // public List<int> MergeTwoLists(List<int> list1, List<int> list2) {
        //     if (list1 == null)
        //     {
        //         return list2;
        //     }
        //     else if (list2 == null)
        //     {
        //         return list1;
        //     }
        //     else if (list1.val < list2.val)
        //     {
        //         list1.next = MergeTwoLists(list1.next, list2);
        //         return list1;
        //     }
        //     else 
        //     {
        //         list2.next = MergeTwoLists(list1, list2.next);
        //         return list2;
        //     }
        // }

        // ================================find length of last word=================================
        // Given a string, find out the length of the last word in the string
        public static int LengthOfLastWord(string sentence)
        {
            int j = 0;

            if(sentence.Length == 1 && sentence[0] != ' ' && sentence[0] != '.' && sentence[0] != '?' && sentence[0] != '!')
            {return j+1;}

            else{
                for(int i = sentence.Length - 1; i > -1; i--)
                {
                    if(sentence[i] != ' ' && sentence[i] != '.' && sentence[i] != '?' && sentence[i] != '!')
                    {j++;}
                    else if (j > 0)
                    {
                        return j;
                    }
                    Console.WriteLine(i);
                }
                return j;
            }
        }
    }
}
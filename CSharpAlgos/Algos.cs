using System;
using System.Collections;
using System.Collections.Generic;

namespace CSharpAlgos
{
    public static class Algos
    {
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
    }
}
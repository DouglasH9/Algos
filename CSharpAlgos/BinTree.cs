using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

namespace CSharpAlgos
{
    public class Node
    {
        public int val {get; set;}
        public Node left {get; set;}
        public Node right {get; set;}
        public Node(int val)
        {
            this.val = val;
        }
    }

    public class BinTree
    {
        private Node _root;
        public BinTree()
        {
            _root = null;
        }
        public void InsertToBinTree(int val)
        {
            // if tree is empty, insert new single Node as the _root
            if (_root == null)
            {
                _root = new Node(val);
                return;
            }
            // if not, recur down the tree...
            InsertRecur(_root, new Node(val));
        }
        private void InsertRecur(Node root, Node newNode)
        {
            if (root == null)
            {
                root = newNode;
            }
            if (newNode.val < root.val)
            {
                if(root.left == null)
                {
                    root.left = newNode;
                }
                else InsertRecur(root.left, newNode);
            }
            else
            {
                if (root.right == null)
                    root.right = newNode;
                else
                    InsertRecur(root.right, newNode);
            }
        }
        private void DisplayBinTreeInOrderTrav(Node root)
        {
            if (root == null) return;
            DisplayBinTreeInOrderTrav(root.left);
            Console.WriteLine(root.val + " ");
            DisplayBinTreeInOrderTrav(root.right);
        }
        public void DisplayBinTreeInOrderTrav()
        {
            DisplayBinTreeInOrderTrav(_root);
        }
    }

}
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

namespace CSharpAlgos
{
    public class Node
    {
        // define attributes of Node
        public int val {get; set;}
        public Node left {get; set;}
        public Node right {get; set;}
        
        // construct Node with int val as parameter
        public Node(int val)
        {
            this.val = val;
        }
    }

    public class BinTree
    {
        // declare valueless Node as _root
        private Node _root;

        // declare BinTree object with _root Node having a value of null
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
        // recursive helper function to recursively insert Nodes
        private void InsertRecur(Node root, Node newNode)
        {
            // insert newNode as root if root is null
            if (root == null)
            {
                root = newNode;
            }

            // if newNode's value is less than the root...
            if (newNode.val < root.val)
            {
                // insert newNode as root.left if root.left is null
                if(root.left == null)
                {
                    root.left = newNode;
                }
                // if root.left is not null recur with root.left as starting node
                else InsertRecur(root.left, newNode);
            }

            // if newNode's val is greater than root...
            else
            {
                // insert newNode into root.right if root.right is null
                if (root.right == null)
                    root.right = newNode;
                
                // otherwise, recur down with root.right and starting Node
                else
                    InsertRecur(root.right, newNode);
            }
        }
        private void DisplayBinTreeInOrderTrav(Node root)
        {
            // if root
            if (root == null) return;
            DisplayBinTreeInOrderTrav(root.left);
            Console.WriteLine(root.val + " ");
            DisplayBinTreeInOrderTrav(root.right);
        }
        public void DisplayBinTreeInOrderTrav()
        {
            DisplayBinTreeInOrderTrav(_root);
        }
        private void DisplayBinTreePreOrderTrav(Node root)
        {

        }
    }

}
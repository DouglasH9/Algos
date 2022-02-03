using System;
using System.Collections.Generic;

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
        public Node _root;

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
            // if root is null return
            if (root == null) return;
            // start with _root traversal
            DisplayBinTreeInOrderTrav(root.left);
            // print the value of root to the console
            Console.WriteLine(root.val + " ");
            // once left branch of tree is done, traverse right side, printing values to console
            DisplayBinTreeInOrderTrav(root.right);
        }
        public void DisplayBinTreeInOrderTrav()
        {
            DisplayBinTreeInOrderTrav(_root);
        }
        public enum BinTreeTraversal
        {
            PreOrder,
            InOrder,
            PostOrder
        }

        public void PrintTree(Node root, BinTreeTraversal treeTraversal)
        {
            Action<int> printValue = delegate(int v)
            {
                Console.WriteLine(v + " ");
            };

            switch (treeTraversal)
            {
                case BinTreeTraversal.PreOrder:
                    PreOrderTraversal(printValue, root);
                    break;
                case BinTreeTraversal.InOrder:
                    InOrderTraversal(printValue, root);
                    break;
                case BinTreeTraversal.PostOrder:
                    PostOrderTraversal(printValue, root);
                    break;
                default: break;
            }
        }

        public void PreOrderTraversal(Action<int> action, Node root)
        {
            if (root == null)
            {
                return;
            }
            action(root.val);
            PreOrderTraversal(action, root.left);
            PreOrderTraversal(action, root.right);
        }

        public void InOrderTraversal(Action<int> action, Node root)
        {
            if (root == null)
            {
                return;
            }
            InOrderTraversal(action, root.left);
            action(root.val);
            InOrderTraversal(action, root.right);
        }

        public void PostOrderTraversal(Action<int> action, Node root)
        {
            if (root == null)
            {
                return;
            }
            PostOrderTraversal(action, root.left);
            PostOrderTraversal(action, root.right);
            action(root.val);
        }

        public List<List<int>> LevelOrderTraversal(Node root)
        {
            // create a List to store a List of values for each level. List of lists.
            List<List<int>> binTreeLevels = new List<List<int>>();
            // call on helper function to recurse through tree and add values to proper Lists
            HelperFunc(root, 0, binTreeLevels);
            // foreach loop to print each level with values to console
            foreach(List<int> level in binTreeLevels)
            {
                Console.WriteLine("_____________");

                for (int i = 0; i < level.Count; i++)
                {
                    Console.WriteLine(level[i]);
                }
            }
            return binTreeLevels;

            // helper function to recurse through tree, will take in root node, level number, and previously declared List of Lists as arguments
            void HelperFunc(Node node, int level, List<List<int>> binTreeLevels)
            {
                // base case. if root of bin tree is null, return
                if (node == null) {return;}

                // check to see if Count of List items is equal to or greater than level, if so, add new empty List to List of Lists
                if (level >= binTreeLevels.Count)
                {
                    binTreeLevels.Add(new List<int>());
                }

                // adds node.val to appropriate level's list
                binTreeLevels[level].Add(node.val);

                // recursive call to .left of current node
                if (node.left != null) {HelperFunc(node.left, level +1, binTreeLevels);}

                // recursive call to .right of current node
                if (node.right != null) {HelperFunc(node.right, level +1, binTreeLevels);}
            }
            
        }
    }
}
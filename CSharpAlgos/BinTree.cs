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
            
        }
    }

}
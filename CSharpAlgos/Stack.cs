using System;
using System.Collections.Generic;

namespace CSharpAlgos
{
    // module that will utilize the STACK data structure for various algos
    public class CircularQueue
    {
        private int[] queue;
        private int headIndex;
        private int count;
        private int capacity;

        public CircularQueue(int n)
        {
            this.capacity = n;
            this.queue = new int[n];
            this.headIndex = 0;
            this.count = 0;
        }

        public bool EnQueue(int val)
        {
            // if queue is full, return false, since there's no more room
            if (this.count == this.capacity)
            {return false;}

            // place new value in the space that is the remainder of the capacity divided by the headIndex + the count
            this.queue[(this.headIndex + this.count) % this.capacity] = val;
            // increase the count by one
            this.count += 1;
            // return true to show that val was inserted
            return true;
        }
    }
}
using System;
using System.Collections.Generic;

namespace CSharpAlgos
{
    // module that will utilize the STACK data structure for various algos
    public class CircularQueueOne
    {
        private int[] queue;
        private int headIndex;
        private int count;
        private int capacity;

        public CircularQueueOne(int n)
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

        public bool DeQueue()
        {
            // return false if there's nothing in the queue to dequeue...
            if (this.count == 0)
            {return false;}

            // move the head index to (head index + 1) % capacity. will keep moving the head index forward by one until the (head index + 1) = capacity, then it will reset the head index to 0
            this.headIndex = (this.headIndex + 1) % this.capacity;
            // subtract 1 from this.count since we removed an element
            this.count -= 1;
            // return true to show that element was successfully removed
            return true;
        }

        public int Front()
        {
            // return a -1 if the queue is empty
            if (this.count == 0) {return -1;}

            // return whatever value is at this.queue[this.headIndex]
            return this.queue[this.headIndex];
        }

        public int Rear()
        {
            // return -1 if queue is empty
            if (this.count == 0){return -1;}

            // set tail index to head index plus the count -1 modulo the capacity. use (count - 1) because the first spot in the queue has an index of zero
            int tailIndex = (this.headIndex + this.count - 1) % this.capacity;
            // return the value of whatever is at this.queue[tailIndex]
            return this.queue[tailIndex];
        }

        public bool IsEmpty()
        // checks to see if queue is empty
        {return (this.count == 0);}

        public bool IsFull()
        // checks to see i queue is full
        {return (this.count == this.capacity);}
    }

    public class CircularQueueTwo
    {
        private int[] data;
        private int head;
        private int tail;
        private int size;

        public CircularQueueTwo(int n)
        {
            this.data = new int[n];
            this.head = -1;
            this.tail = -1;
            this.size = n;
        }

        public bool EnQueue(int val)
        {
            if (this.IsFull() == true){return false;}

            if (this.IsEmpty() == true){this.head = 0;}

            this.tail = (this.tail + 1) % this.size;
            this.data[tail] = val;
            return true;
        }
        public bool DeQueue()
        {
            if (this.IsEmpty() == true){return false;}
            if (this.head == this.tail) 
            {
                this.head = -1;
                this.tail = -1;
                return true;
            }
            this.head = (this.head +1) % this.size;
            return true;
        }
        public int Front()
        {
            if (this.IsEmpty() == true){return -1;}

            return this.data[head];
        }
        public int Rear()
        {
            if (this.IsEmpty() == true){return -1;}

            return this.data[tail];
        }
        public bool IsEmpty()
        {
            return this.head == -1;
        }
        public bool IsFull()
        {
            return ((this.tail + 1) % this.size) == head;
        }
    }
}
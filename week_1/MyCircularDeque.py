class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """

        self.front = 0
        self.rear = 0
        self.capacity = k + 1
        self.arr = [0 for _ in range(self.capacity)]

    def insert_front(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """

        if self.is_full():
            return False
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.arr[self.front] = value
        return True

    def insert_last(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """

        if self.is_full():
            return False
        self.arr[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        return True

    def delete_front(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.is_empty():
            return False
        self.front = (self.front + 1) % self.capacity
        return True

    def delete_last(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """

        if self.is_empty():
            return False
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        return True

    def get_front(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.is_empty():
            return -1
        return self.arr[self.front]

    def get_rear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """

        if self.is_empty():
            return -1
        return self.arr[(self.rear - 1 + self.capacity) % self.capacity]

    def is_empty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.front == self.rear

    def is_full(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return (self.rear + 1) % self.capacity == self.front

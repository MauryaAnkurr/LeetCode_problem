#Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

#Implement the MovingAverage class:

#MovingAverage(int size) Initializes the object with the size of the window size.
#double next(int val) Returns the moving average of the last size values of the stream.

class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.size =size
        self.queue = [0]*self.size
        self.head = self.window_sum=0
        self.count =0
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.count +=1
        tail = (self.head+1) % self.size
        self.window_sum =self.window_sum-self.queue[tail]+val
         
        self.head = (self.head + 1) % self.size
        
        self.queue[self.head] = val
        return float(self.window_sum / float(min(self.size, self.count)))

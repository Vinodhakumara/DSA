# Recursion
class Recursion: 
    '''Recursion'''
    def __init__(self):
        pass
    
    def fact(n):  # Factorial
        '''Recursion: Factorial'''
        if n < 0 and int(n) != n:
            return "Not supported"
        elif n == 0:
            return 1
        else:
            return n * recursion.fact(n-1)
     
    def fib(n):
        '''Recursion: Fibonacci'''
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n-1)+fib(n-2)
    
        
# Searching
class Search:
    '''Searching a element'''
    def __init__(self):
        search = int()
    
    def linear(db,search):  # linear Search
        '''Search: Linear Search
           Method:'''
        pos = 0
        lib = list()
        while pos < len(db):
            if db[pos] == search:
                lib.append(pos)
            pos = pos + 1
        if lib == []:
            result = "Not found!"
        else:
            result = lib
        return result
        
    def binary(db , search):  # Binary Search
        '''Search: Binary Search
           Method: 
           '''
        if not sort.checkSorted(db):
            first = 0
            end = len(db) - 1
            middle = int(first + end / 2)
            while not (db[middle] == search) and first <= end :
                if db[middle] < search :
                    first = middle + 1
                else :
                    end = middle - 1
                middle = int((first + end) / 2)
            if db[middle] == search:
                return "Searching element {} found at {}".format(search,middle)
            else:
                return ("Not found")
        else:
            return "Elements not Sorted!!"
            
# Sorting
class Sort:
    """ Sorting in Ascnding or Discending order"""
    def __init__(self):
        notSorted = False
        
    # Sorted or not
    def checkSorted(db):
        '''Check whether sorted or not'''
        for i in range(1,len(db)):
            if db[i-1] > db[i]:
                return True
        return False
    
    def bubble(db):  # Bubble Sort
        '''Sort: Bubble Sort
           Method: Exchange Algo
           Formula: '''
        isswap = False
        for j in range(len(db)-1):
            for i in range(len(db)-1):
                if db[i] > db[i+1]:
                    isswap = True
                    db[i] , db[i+1] = db[i+1],db[i]
        if not isswap:
            return ("\n\t\t  Already Sorted")
        else:
            return db
        
    def selection(db):  # Selection Sorting
        '''Sort: Selection Sort
           Method: Selection Algo
           Formula: '''
        if sort.checkSorted(db) :
            for i in range(len(db)):
                min_val = i
                for z in range(i+1,len(db)):
                    if db[min_val] > db[z]:
                        min_val = z
                db[i], db[min_val] = db[min_val],db[i]
            return db
        else:
            return ("Already Sorted")
    
    def insertion(db):  # Insertion Sorting 
        """ Sort: Insertion Sorting 
            Method: Inplace algo  
            Formula: [(n*(n+1))/2]"""
        for i in range(1,len(db)):
            if db[i-1] > db[i]:
                notSorted = True
                break
        if sort.checkSorted(db) :
            for i in range(1,len(db)):
                pos = i
                curVal = db[i]
                while pos > 0 and db[pos-1] > curVal:
                    db[pos] = db[pos-1]
                    pos = pos - 1
                db[pos] = curVal
            return db
        else:
            return ("Already Sorted")

# Stack: LIFO(Last In First Out)
class Stack:
    def __init__(self):
        self.stack = stack
    # Push to Stack
    def push(self,elem):
        self.stack.append(elem)
    # Remove(pop) from Stack
    def pop(self):
        isEmp = self.isEmpty() 
        if isEmp[0]:
            return isEmp[1]+" Can't pop!"
        self.stack.pop()
    # Check Stack is empty or not
    def isEmpty(self):
        return (True,("Stack is empty!")) if self.queue == [] else (False,("Stack is not empty!"))
    # Show Peak Value
    def peek(self):
        return self.stack[len(stack)-1]
    # Print Stack
    def printStack(self):
        self.stack.reverse()
        for i in self.stack:
            print(i)
    # Print string when object run string prints: Print Stack
    def __str__(self):
        self.stack.reverse()
        mystack=[]
        for i in self.stack:
            mystack.append(i)
        self.stack.reverse()
        return "\n".join(mystack)
    
# Queue FIFO(First In First Out)
class Queue:
    def __init__(self,queue):
        self.queue=queue
    # Add Element to a queue
    def push(self,elem):
        self.queue.append(elem)
    # Remove Element from queue
    def pop(self):
        isEmp = self.isEmpty() 
        if isEmp[0]:
            return isEmp[1]+" Can't pop!"
        self.queue.pop(0)
    def peak(self):
        return self.queue[0]
    def isEmpty(self):
        return (True,("Queue is empty!")) if self.queue == [] else (False,("Queue is not empty!"))
    # Print a Queue
    def printQueue(self, queue=None):
        myqueue=""
        if queue != None:
            for i in queue:
                myqueue+=str(i)+"\n"
            return myqueue
        else:
            for i in self.queue:
                myqueue+=str(i)+"\n"
            return myqueue
    def __str__(self):
        myqueue=""
        for i in self.queue:
            myqueue+=str(i)+"\n"
        return myqueue
class Queue:
  def __init__(self):
    self.queue=[]
    
  #Returns False if the queue has at least one element (length of list > 0) and return True if the length of list == 0
  def is_empty(self):
    if len(self.queue)>0:
      return False
    else:
      return True
      
  #Adds an element to the end of the queue
  def enqueue(self, element):
    self.queue.append(element)
    return self.queue
  #Checking if the queue is empty then send a warning message. Else lets remove the first element of the queue.
  def dequeue(self):
    if self.is_empty():
      return "The queue is empty"
    else:
      return self.queue.pop(0)
  
  #Return the value of the front of the queue without removing it but first we check if the queue is empty
  def peek(self):
    if self.is_empty():
      return "The queue is empty"
    else:
      return self.queue[0]

  def size(self):
    return len(self.queue)
      
# Instantiating the queue
q=Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

#Display first element
print("Queue first element: ",q.peek())
# Displays the removed element
print("The element ",q.dequeue()," is removed from the Queue")

print("Queue first element: ",q.peek())

print("size of the queue: ", q.size())
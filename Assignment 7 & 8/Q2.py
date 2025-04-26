class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")
    
    def dequeue(self):
        if not self.is_empty():
            removed_item = self.queue.pop(0)
            print(f"Dequeued: {removed_item}")
            return removed_item
        else:
            print("Queue is empty")
            return None
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue:", " <- ".join(map(str, self.queue)))

# Example usage:
if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.display()
    q.dequeue()
    q.display()

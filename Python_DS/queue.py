class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        #adding to the front of the list (.insert)
        self.items.insert(0, item)

    def dequeue(self):
        #removing the last element in list
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
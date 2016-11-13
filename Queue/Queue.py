# -*- coding: utf-8 -*-
class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self, items):
        self.items.append(items)

    def dequeue(self):
        return self.items.pop(0)

    def empty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)

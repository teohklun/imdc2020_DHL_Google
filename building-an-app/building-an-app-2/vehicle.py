import itertools

class Vehicle:
    def func(self):
        print('Hello')
        
    def __init__(self,id, start, capacity, skills, time_window = None, end = None, name=None):
        self.id = id
        self.start = start
        self.capacity = capacity
        self.skills = skills
        self.time_window = time_window
        self.name = name
        self.end = end
        #self._id = 1

    def getID(self):
        return self.id
        
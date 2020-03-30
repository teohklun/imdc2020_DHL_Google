import itertools

class Job:
    def func(self):
        print('Hello')
        
    def __init__(self,id, delivery, location, skills, time_windows,service=None, description=None):
        self.id = id
        self.delivery = delivery
        self.location = location
        self.skills = skills                
        self.time_windows = time_windows
        self.service = 300
        self.description = description
#         self.street=street
        
    def getID(self):
        return self.id
        
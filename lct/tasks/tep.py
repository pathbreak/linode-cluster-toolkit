import json
import uuid

class TaskExecutionPlan(object):
    
    def __init__(self, tk, name):
        '''
        Arguments:
          tk - The Toolkit object for access to all services, especially
            the task service which this class uses for persistence.
          
          name - A name for this task execution plan. It gets displayed
            when user queries for current list of operations.
        '''
        self._tk = tk
        self.name = name
        self.uuid = uuid.uuid1()
        
        self._tasks = []
        
        
        
        
    def add(self, task):
        self._tasks.append(task)
        
        
        
    def save(self):
        self.tk.task_service().save_execution_plan(task_plan)

            
            
class TestTask1(object):
    def __init__(self):
        self._details = {
            'cluster' : 'cluster1',
            'region' : 9,
            'type' : 'g5-nanode'
        }
    
    def details(self):
        return self._details
        
        
        
class TestTask2(object):
    def __init__(self):
        self._details = {
            'cluster' : 'cluster2',
            'region' : 8,
            'type' : 'g5-standard'
        }
    
    def details(self):
        return self._details



    

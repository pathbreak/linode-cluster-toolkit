from pymongo import MongoClient

class MongoTaskStore(TaskStore):
    '''
    A TaskStore implementation to store task execution plans and their
    status in MongoDB.
    '''
    
    def initialize(self):
        '''
        Initialization opportunity for providers.
        This is called when the toolkit itself and all services, including
        the Task Service, are initializing themselves.
        '''
        self._client = MongoClient(w=1, j=True)

        self._db = client.test 
        
        
        
    def close(self):
        '''
        Provider should release its resources here.
        '''
        self._client.close()


    
    def save_execution_plan(self, task_plan):
        '''
        Save or update the execution plan.
        '''
        raise NotImplementedError('subclasses should override this')





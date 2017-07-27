class TaskStore(object):
    '''
    All task execution plans are stored and tracked in a TaskStore.
    Both are crucual for supporting pause and resume of operations.
    
    The interface to be implemented by all providers that provide task
    storage capabilities.  
    '''
    
    def initialize(self):
        '''
        Initialization opportunity for providers.
        This is called when the toolkit itself and all services, including
        the Task Service, are initializing themselves.
        '''
        raise NotImplementedError('subclasses should override this')
        
        
        
    
    def save_execution_plan(self, task_plan):
        '''
        Save or update the execution plan.
        '''
        raise NotImplementedError('subclasses should override this')



    def close(self):
        '''
        Provider should release its resources here.
        '''
        raise NotImplementedError('subclasses should override this')

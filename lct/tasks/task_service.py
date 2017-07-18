class TaskService(object):
    '''
    Provides task queuing, parallel execution, retrying, and error handling of tasks
    for the toolkit itself and for clients of the toolkit.
    
    It delegates actual task management to a task provider implementation
    instantiated according to provided toolkit configuration. 
    '''
    
    
    
    def __init__(self):
        self._initialized = False



        
    def initialize(self, tk):
        '''
        Perform all initializations, including asking required collaborator
        services to initialize themselves if they haven't already.
    
        initialize may be invoked multiple times due to other services 
        which require this service to be initialized.        
        '''
        
        if self._initialized:
            return
            
        self.tk = tk
        
        
        self._initialized = True

        
    def close(self):
        pass
        
    
    
    ####################### FUNCTIONALITY: #############################
    
    
    



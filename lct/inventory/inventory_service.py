class InventoryService(object):
    '''
    Interface for storing and querying cluster information. 
    The interface is implemented by different storage providers which
    can store data in structured text files or relational or NoSQL databases
    or any other storage backend.
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

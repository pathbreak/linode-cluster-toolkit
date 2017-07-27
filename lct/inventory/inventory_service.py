class InventoryService(object):
    '''
    Interface for creating and providing an inventory implementation provider
    that stores cluster and node information, and supports queries on them.
    
    Use InventoryService.provider() to get the interface to store and query
    inventory information.
    
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

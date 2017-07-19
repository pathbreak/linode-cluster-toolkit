class ToolkitTask(object):
    '''
    A base class for provisioning and configuration operations that
    should be executed by the task service.
    '''
    
    
    
    def __init__(self, tkctx):
        '''
        Construct the task, giving the application+customer scoping context 
        in which the task should be executed.
        
        Arguments:
          tkctx - The toolkit context in which the task's operations should
            be executed.
        '''
        self.tkctx = tkctx
    
    
    
        
    def execute(self):
        raise NotImplementedError('Subclasses should override execute')
        
        
        
        
        

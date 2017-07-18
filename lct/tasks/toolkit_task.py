class ToolkitTask(object):
    '''
    A base class for provisioning and configuration operations that
    should be executed by the task service.
    '''
    
    
    
    def __init__(self):
        pass
    
    
    
        
    def execute(self):
        raise NotImplementedError('Subclasses should override execute')

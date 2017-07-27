class ToolkitTask(object):
    '''
    A base class for provisioning and configuration operations that
    should be executed by the task service.
    
    To support pause and resume workflow, every ToolkitTask should 
    provide a serializable 'params' dict which contains all the details
    it requires to execute when provided at a later point in time.
    
    Every task may model its operations as subtasks of its own if it requires
    pause and resume at the subtask level. The subtasks will get executed
    serially in the order in which they have been added.
    '''
    
    
    
    def __init__(self, tkctx, params):
        '''
        Construct the task, giving the application+customer scoping context 
        in which the task should be executed.
        
        Arguments:
          tkctx - The toolkit context in which the task's operations should
            be executed.
            
          params - A dict with all the parameters required for the task
            to execute. This is provided either by a cluster operation
            or loaded from the task execution plan database because of a 
            resume operation request after it was paused.
        '''
        self.tkctx = tkctx
        self._params = params
    
    
    
    def params(self):
        '''
        Returns the params dict that contains all the information required
        by this task to execute at any point of time.
        '''
        return self._params
        
        
        
    def subtasks(self):
        '''
        Return the subtasks that comprise this task if the task is to be modelled
        as a sequence of subtasks. If the task does not require or does not
        prefer such modelling, it should just return None.
        '''
        return None
        
        
        
    def execute(self):
        '''
        Execute the operations of this task.
        '''
        raise NotImplementedError('Subclasses should override execute')
        
        
        
        
        

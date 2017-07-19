class TaskExecutor(object):
    '''
    Interface to be implemented by task exection providers.
    '''

    def initialize(self, tk):
        raise NotImplementedError('subclasses should override this')
        
    def close(self):
        raise NotImplementedError('subclasses should override this')
        
    
    def submit_task(self, task):
        '''
        Submit a task for execution.
        
        An executor can examine the task's toolkit context (task.tkctx)
        to select a particular queue or other suitable strategy
        
        Arguments:
          task : ToolkitTask - A task that encapsulates the operation 
            or sequence of operations to be executed by the task queue.
        '''
        raise NotImplementedError('subclasses should override this')

        

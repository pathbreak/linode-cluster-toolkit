from lct.tasks.task_executor import TaskExecutor

class ImmediateExecutor(TaskExecutor):
    '''
    This provider executes the task immediately as it's received, blocking
    the caller thread. There is no queue being used.
    Suitable for creation of very small clusters and single nodes by
    single threaded command-line clients, applications and scripts.
    
    Implementation Notes:
    - This is thread-safe in the sense that it blocks any caller while
      executing a task. Tasks can be submitted from multiple threads and
      they get executed in the same thread as the caller.
    - This does not implement any rate limiting.
    - 
    '''
    
    def __init__(self):
        self._initialized = False
        
    
    def initialize(self, tk):

        if self._initialized:
            return
            
        self._initialized = True


        
    def close(self):
        pass
 
 
        
    def submit_task(self, task):
        '''
        Submit a task for execution.
        
        This implementation simply calls the task's execute function.
        
        Arguments:
          tkctx : ToolkitContext - The application and customer context
            for this task. 
            This provider ignores the values in this argument. There's only
            one queue for all apps and all customers.
            
          task : ToolkitTask - A task that encapsulates the operation 
            or sequence of operations to be executed by the task queue.
            ``task.tkctx`` provides the application and customer context
            for this task. 
        '''
        try:
            # Execute the task immediately.
            task.execute()
            
            # TODO If task is successful, the notify caller 
            # via a provided callback.
        except:
            # TODO If there's an error, notify caller 
            # via a provided callback.
            pass
        
        
        
    
    

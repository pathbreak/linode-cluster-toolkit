try:
    # Python 3 queue
    import queue
except ImportError:
    # Python 2 Queue
    import Queue as queue
    
import threading

class MultiThreadExecutor(TaskExecutor):
    '''
    A simple multithreaded producer-consumer queue-based implementation, 
    suitable for creation of
    small clusters and single nodes by
    single threaded command-line clients, applications and scripts.
    
    Implementation Notes:
    - This is thread-safe. Tasks can be submitted from multiple threads.
    - Tasks are held in a thread-safe queue.
    - Number of executor threads is controlled from toolkit configuration. 
    - There are no sequential guarantees for tasks of same consumer, because
      any executor thread can execute them. 
      If operations should be conducted in a sequence, make them part of the
      same Task.
    - This does not implement any rate limiting.
    '''
    
    def __init__(self):
        self._initialized = False
        
    
    def initialize(self, tk):

        if self._initialized:
            return
            
        # Do initializations here.
        # TODO Read configuration and create queues and threads
        # based on settings there.
        self._q = queue.Queue()
        self._worker = threading.Thread(target = self._task_executor)
            
        self._initialized = True


        
    def close(self):
        # Put the poison pill in queue to kill worker thread, and wait
        # for queue and worker thread to terminate themselves.
        self._q.put(None)
        self._q.join()
        self._worker.join()
 
 
        
    def submit_task(self, task):
        '''
        Submit a task for execution.
        
        Arguments:
          tkctx : ToolkitContext - The application and customer context
            for this task. 
            This provider ignores the values in this argument. There's only
            one queue for all apps and all customers.
            
          task : ToolkitTask - A task that encapsulates the operation 
            or sequence of operations to be executed by the task queue.
        '''
        pass
        
    ########################## PRIVATE #########################
        
    def _task_executor(self):
        
        
    
    

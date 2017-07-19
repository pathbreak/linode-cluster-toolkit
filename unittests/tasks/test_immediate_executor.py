from __future__ import print_function

import unittest


from lct.tasks.immediate_executor import ImmediateExecutor
from lct.tasks.toolkit_task import ToolkitTask
from lct.toolkit import ToolkitContext



class TestImmediateExecutor(unittest.TestCase):
    
    def test_submit_task(self):
        exec = ImmediateExecutor()
        exec.initialize(None)
        
        task = TestTask()
        exec.submit_task(task)
        
        
        
class TestTask(ToolkitTask):
    def __init__(self):
        pass
        
    def execute(self):
        print(42)
   
if __name__ == '__main__':
    unittest.main()

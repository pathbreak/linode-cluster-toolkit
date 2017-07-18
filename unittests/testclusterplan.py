import unittest
import os

from lct.clusters.clusterplan import ClusterPlan

class TestClusterPlan(unittest.TestCase):
    
    def test_load_from_yaml(self):
        plan = ClusterPlan.load_from_yaml(os.path.dirname(__file__) + '/testplan1.yaml')
        self.assertIsNotNone(plan)
        #print(plan.regions())
        for r in plan.regions():
            #print(r.region, r.nodes)
            for nodeplan in r.nodes:
                print(nodeplan.name, nodeplan.type)
                if nodeplan.storage is not None:
                    for disk in nodeplan.storage:
                        print(disk.type)
        
        
    def test_load_from_json(self):
        plan = ClusterPlan.load_from_json(os.path.dirname(__file__) + '/testplan1.json')
        self.assertIsNotNone(plan)
        print(plan.regions())
    
if __name__ == '__main__':
    unittest.main()

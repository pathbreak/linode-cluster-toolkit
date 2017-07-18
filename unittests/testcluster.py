import unittest
import os

from clusterplan import ClusterPlan
from cluster import Cluster

class TestCluster(unittest.TestCase):
    
    def test_create(self):
        plan = ClusterPlan.load_from_yaml(os.path.dirname(__file__) + '/testplan1.yaml')
        self.assertIsNotNone(plan)
        cluster = Cluster()
        cluster.create(plan)
        
   
if __name__ == '__main__':
    unittest.main()

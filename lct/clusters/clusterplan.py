from __future__ import print_function

import yaml
import json
import codecs

class ClusterPlan(object):
    
    def __init__(self, plandict):
        self.plan = plandict

        self._check_plan()

        self._init_from_dict()
    
    @classmethod
    def load_from_json(clz, filename):
        with open(filename, 'r') as json_file:
            plan = json.load(json_file)
            
        return ClusterPlan(plan)
        
    @classmethod    
    def load_from_yaml(clz, filename):
        #with open(filename, 'r') as yaml_file:
        with codecs.open(filename, 'r', encoding="utf-8") as yaml_file:
            plan = yaml.safe_load(yaml_file)
            
        return ClusterPlan(plan)
        
        
    def regions(self):
        return self._regions
        
            
            
    #===================================================================
    
    
    def _check_plan(self):
        if self.plan is None:
            raise RuntimeError('self.plan not set')
            
            
    def _init_from_dict(self):
        self.name = self.plan['name']
        
        self._regions = []
        for r in self.plan['regions']:
            nodeplans = []
            for n in r['nodes']:
                nodeplan = type('NodePlan',(object,),n)()
                # count is not mandatory. If there's no count, assume count of 1.
                nodeplan.count = n.get('count', 1)
                
                storage = n.get('storage', 'default')
                if storage == 'default':
                    nodeplan.storage = None
                else:
                    disks = []
                    for s in storage:
                        disk = type('Disk',(object,),s)()
                        disks.append(disk)
                    nodeplan.storage = disks
                
                nodeplans.append(nodeplan)
            
            r['nodes'] = nodeplans

            region = type('Region',(object,),r)()
            self._regions.append(region)
            
            
        

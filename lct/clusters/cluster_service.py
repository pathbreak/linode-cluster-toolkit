import uuid

from lct.tasks.toolkit_task import ToolkitTask
from lct.tasks.tep import TaskExecutionPlan

class ClusterService(object):
    '''
    The Cluster Service provides cluster provisioning, configuration and  
    orchestration services to clients of the toolkit and to other
    internal services which may need them.
    
    The application or customer context should be provided to each cluster 
    operation by passing in the correct ToolkitContext.  
    '''
    
    def __init__(self):
        self._initialized = False
        
        
        
    
    def initialize(self, tk):
        '''
        Perform all initializations, including asking required collaborator
        services to initialize themselves if they haven't already.
    
        initialize may be invoked multiple times due to other services 
        which require this service to be initialized.        
        '''
        
        if self._initialized:
            return
            
        self.tk = tk
        
        # Make sure all required services are initialized.
        self.tk.api_service().initialize(self.tk)
        self.tk.inventory_service().initialize(self.tk)
        
        
        self._initialized = True
        
        
        
    def close(self):
        pass
        
        
        
    #======================== FUNCTIONALITY: ==========================
        
        

    def create_cluster(self, tkctx, cluster_plan, app_defn_cluster_name, app_defn_cluster_id):
        '''
        Creates a cluster based on given cluster_plan.
        
        Args:
          tkctx: A ToolkitContext object that provides the application & customer context
            for the newly created cluster.
            
          cluster_plan: A ClusterPlan object describing the plan for the cluster
        
          app_defn_cluster_name: An application provided name for this cluster.
          
          app_defn_cluster_id: str An optional application provided identifier string for this cluster.
            Note that this is not used by the toolkit, just stored and included
            back in results for the application to use. The toolkit generates its own UUID
            and provides that too in results. Applications should use the toolkit-generated UUID when
            querying for cluster information.
            It can be a numeric or alphanumeric or path-like string - the toolkit doesn't
            impose any validations.
            
        Returns:
          A Cluster object that provides access to all the nodes or other resources
          of newly created cluster.
        '''
        cluster = Cluster()
        cluster.uuid = uuid.uuid1()
        cluster.app_defn_cluster_name = app_defn_cluster_name
        cluster.app_defn_cluster_id = app_defn_cluster_id
        
        # - Walk through every region in the plan
        #
        # - each region consists of multiple node plans, specifying the linode
        #   type, counts, their storage plans, and node initialization options.
        #
        # - a node creation involves not just the creation of node using Linode API,
        #   but depending on the plan, additional operations like 
        #     > creating a disk from an image 
        #     > configuring a disk using a stackscript or cloud-init or Ansible
        #     > linode config creation
        #     > first boot up
        #     > post-first-boot configurations like users, groups, security hardening, etc.
        #     > persisting of node details to inventory storage
        #
        # - Some tasks are parallelizable. For example, two different end-to-end node creations
        #   can be done in parallel (with API rate limits being the only exception). But some
        #   sub tasks in each node creation may have to be executed in sequence because result of
        #   one is input to next.
        #
        # - Anything that can be executed concurrently is done so via the task
        #   queue service. It's upto the toolkit configuration and task queue logic to decide
        #   the actual parallelism of tasks.
        
        
        task_plan = TaskExecutionPlan(
            self.tk, 
            'create cluster {} ({})'.format(cluster.app_defn_cluster_name, cluster.uuid))
        
        for r in cluster_plan.regions():
            for nodeplan in r.nodes:
                print('Create {0} nodes of type {1} in region {2}'.format(nodeplan.count, nodeplan.type, r.region))

                # Create concurrent node creation+initialization+store task
                # for each node.
                for i in range(nodeplan.count):
                    # TODO fill params
                    params = {}
                    node_task = SingleNodeCreationTask(params)
                    task_plan.add(node_task)
                    
        # Persist this task plan to database so we can track it.
        task_plan.save()

        return cluster



class SingleNodeCreationTask(ToolkitTask):
    '''
    A task for the end-to-end provisioning of a single node.
    '''
    
    
    def __init__(self, tk, tkctx, region, parent_nodeplan, cluster, cluster_plan):
        super(SingleNodeCreationTask, self).__init__(tkctx)
        
        self.tk = tk
        self.region = region
        self.parent_nodeplan = parent_nodeplan
        self.cluster = cluster
        self.cluster_plan = cluster_plan
        
    
    def execute(self):
        
        # All the steps involved in the creation of a single node just to
        # streamline my own thinking 
        
        # TODO support all the different ways of node initialization here.
        # For now, just the simplest stock distribution based one.
        
        
        # Attempt to create the node. If the plan specifies default disk allocation
        
        '''
        if self.nodeplan.storage == None:
            create_result = api_service.create_node(region, type, label, group, distribution, 
                stackscript, stackscript_data, root_pass, root_ssh_key) 
        else:
            # TODO We need to create disks and volumes according to a custom storage plan and possibly 
            # format filesystems which are tasks to be done at boot up or after SSH bringup.
            pass
            
        if not create_result:
            # Add the task to a list of failed tasks to be tried again manually.
            # All the context necessary to retry the task should be stored in the list.
            error_service.add_failed_task(task)
            return
            
        if node requires immediate configuration:
            # This will execute any boot-time configurations such as stack scripts or 
            # cloud-init or local ansible on the node itself.
            api_service.boot_node()
            
            # This will execute any post-first-boot node level remote configuration from the host the toolkit
            # is running on to the newly created node.
            config_service.first_boot_configuration()
            
            api_service.shutdown_node()
            
        else:
            # post-first-boot node level configuration should be executed at node boot probably at cluster
            # start.
            pass
            
        inventory_service.add_node(tkctx, cluster, node)
        '''
        pass
        



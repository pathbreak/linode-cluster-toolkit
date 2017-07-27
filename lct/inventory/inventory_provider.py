class InventoryProvider(object):
    '''
    Interface to be implemented by inventory providers for storing
    and querying cluster states, information about nodes, and other
    resources.
    '''
    
    # ====================== Cluster Operations ========================
    
    
    def new_cluster(self, cluster):
        '''
        Initialize storage for information about a new cluster.
        
        Arguments:
          cluster - A `lct.clusters.cluster.Cluster` object with a .uuid field.
        '''
        
        raise NotImplementedError('subclasses should override this')
        
        
        
    def update_cluster_state(self, cluster):
        '''
        Updates the current state of the cluster in inventory.
        
        Arguments:
          cluster - A `lct.clusters.cluster.Cluster` object with a .uuid field
            and a .state field with the new state.
        '''
        
        raise NotImplementedError('subclasses should override this')
    
    
        
    def delete_cluster(self, cluster):
        '''
        Delete **all** information about given cluster from inventory.
        
        Arguments:
          cluster - A `lct.clusters.cluster.Cluster` object with a .uuid field.
        '''
        
        raise NotImplementedError('subclasses should override this')
    
    
    
    # ====================== Node Operations ========================
    

    def add_node(self, cluster, node):
        '''
        Store or update information about a node in inventory.
        
        Arguments:
          cluster - A `lct.clusters.cluster.Cluster` object with a .uuid field.
          
          node - A `lct.clusters.node.Node` object with a .id field and other details to 
            be stored.
        '''
        
        raise NotImplementedError('subclasses should override this')
        
        
        
    def update_node_state(self, cluster, node):
        '''
        Updates the current state of the node in inventory.
        
        Arguments:
          cluster - A `lct.clusters.cluster.Cluster` object with a .uuid field
            and a .state field with the new state.

          node - A `lct.clusters.node.Node` object with new state.
        '''
        
        raise NotImplementedError('subclasses should override this')
        
    
    
    def delete_node(self, cluster, node):
        '''
        Delete details of a node from inventory.
        
        Arguments:
          cluster - A `lct.clusters.cluster.Cluster` object with a .uuid field.
          
          node - A `lct.clusters.node.Node` object with a .id field that identifies
            it.
        '''
        
        raise NotImplementedError('subclasses should override this')
        
        
        
    
    
    
    

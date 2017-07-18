
class Cluster(object):
    '''
    A Cluster represents a cluster of nodes that work together to provide
    some functionality, such as file storage or database or data processing or 
    web serving.
    
    There are multiple names and identifiers for a cluster. 
    - The toolkit generates a UUID which has very high guarantees of being unique across
    applications and customer accounts. 
    - Every application can also provide an application-defined identifier 
      and friendly 'name'.
    '''
    
    
    def __init__(self):
        # Just declaring the attributes of a Cluster here.
        # These are set by the services.
        self.uuid = None
        self.app_defn_cluster_name = None
        self.app_defn_cluster_id = None
        
                


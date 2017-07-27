
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
        self.state = ClusterState()
        self.app_defn_cluster_name = None
        self.app_defn_cluster_id = None
        
                

class ClusterState(object):
    '''
    The different states a cluster can be in as a whole.
    
    Implementation notes:
    Since the state of a cluster gets persisted, these values are implemented 
    as strings to aid readability of stored data, and to avoid mistakes
    like adding a new state with an existing numeric value which would make an
    already stored state inconsistent with its new interpretation in code.
    '''
    
    DOES_NOT_EXIST = 'notexist'
    CREATING =  'creating'
    CREATED = 'created'
    STARTING = 'starting'
    STARTED = 'started'
    STOPPING = 'stopping'
    STOPPED = 'stopped'
    DESTROYING = 'destroying'
    DESTROYED = 'destroyed'
    
    def __init__(self):
        self._state = ClusterState.DOES_NOT_EXIST

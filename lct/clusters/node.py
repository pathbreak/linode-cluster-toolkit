class Node(object):
    '''
    A Node object represents a Linode server.
    '''
    
    def __init__(self):
        self.id = None # the linode ID (integer
        self.state = NodeState() # the NodeState
        self.tags = []
        
        
class NodeState(object)
    # TODO Lifetime states like first boot completed should be tracked independent of current
    # node state. Similarly, configuration states too should be tracked
    # I think.
    
    DOES_NOT_EXIST = 'notexist'
    CREATING = 'creating'
    CREATED = 'created'
    STARTING = 'starting'
    STARTED = 'started'
    STOPPING = 'stopping'
    STOPPED = 'stopped'
    DESTROYING = 'destroying'
    DESTROYED = 'destroyed'
    
    # Has the node never been booted or has it been booted atleast once?
    # The first boot is important for initial node configuration.
    NEVER_BOOTED = 'notbooted'
    FIRST_BOOT_COMPLETED = 'firstbooted'
    
    # Additionally, has the node never undergone any configuration steps,
    # or has it atleast undergone initial, post-provisioning configuration steps?
    # 
    # TODO Other configuration steps related to cluster states and cluster
    # orchestration require more advanced state tracking than these "yes/no" 
    # states.
    NOT_CONFIGURED = 'notconfigured'
    INITIAL_CONFIGURED = 'initconfigured'
    
    def __init__(self):
        self.state = NodeState.DOES_NOT_EXIST
        self.boot_state = NodeState.NEVER_BOOTED
        self.conf_state = NodeState.NOT_CONFIGURED
    

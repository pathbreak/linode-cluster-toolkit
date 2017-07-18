import requests

class APIService(object):
    '''
    Wrapper for Linode's APIs and SDK.
    
    Uses the v4 API python SDK (https://github.com/linode/python-linode-api) 
    whenever possible, but also uses raw v4 REST requests or v3 API if they're useful
    (for example, as of July 2017, there are no v4 image management APIs while v3 has
    them).
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
        
        self._initialized = True
        
        
    def close(self):
        pass
        
        
    #=============================== FUNCTIONALITY =====================
    
    def create_node(self):
        # Note: v4 API 'create' does not boot the linode, only creates linode,
        # disks and a config.
        pass
        
    

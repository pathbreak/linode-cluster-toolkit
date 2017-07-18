class SecretsService(object):
    '''
    Interface for storing and querying secrets such as API keys,
    passwords or SSH private keys.
    
    This service delegates actual secrets management to a management provider via a secrets 
    provider interface. The provider to be used can be configured in the ToolkitConfiguration
    and can be anything from a production grade provider like HashiCorp Vault to a 
    simple insecure text-file based provider.
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
        
        # Create the secrets provider here according to toolkit configuration.
        
        self._initialized = True

        
    def close(self):
        pass
    

    ######################## FUNCTIONALITY =============================
    
    
    
    def store_api_key(self, tkctx, api_key):
        pass

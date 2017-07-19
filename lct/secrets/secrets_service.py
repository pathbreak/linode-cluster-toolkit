import importlib
from lct.utils.dpath_utils import dpath_get
from lct.utils.dynamic_class_loader import instantiate

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
        provider_class_name = dpath_get(tk.conf, 'secrets/provider', 
            'lct.secrets.simple_secrets_provider.SimpleSecretsProvider')
        
        self._provider = instantiate(provider_class_name)
        self._provider.initialize(tk)
        
        
        self._initialized = True

        
    def close(self):
        self._provider.close()
    

    ######################## FUNCTIONALITY =============================
    
    
    
    def provider(self):
        return self._provider

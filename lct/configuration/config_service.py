class ConfigurationService(object):
    '''
    Interface for performing configuration tasks, with support for multiple
    techniques such as stackscripts, cloud-init, and local & remote Ansible.
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

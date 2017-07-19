class LinodeInfoService(object):
    '''
    A lot of information about Linode cloud is relatively unchanging but also required 
    frequently by other services, such as the list of 
    regions/datacenters/kernels/distributions/types/configurations/pricing.
    
    This service fetches and caches such information, provides it to other services and to
    toolkit clients, and provides options to update the cache.
    
    Implementation Details:
    The v3 API's avail.* endpoints as well as v4 API's endpoints for these data
    support fetching them without authentication. But the v4 python library 
    does not. So this service gets it using raw requests via the api_service.
    '''
    
    
    def __init__(self):
        self._initialized = False
        
        self._regions = None



        
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
        
        
        # Depending on the conf in tk.conf, optionally update cache on every startup or
        # every x days since previous update. Then load from cache into memory and serve
        # everything from memory.
        
        
        
        self._initialized = True

        
    def close(self):
        pass
        
        
    # ========================== FUNCTIONALITY =========================
    
    def get_creation_rate_limit(self):
        '''
        Get the current rate limit on node creation.
        
        Returns:
          (limit : int, timeperiod_in_seconds : int) - A tuple of the 
          maximum number of creation operations and the time period 
          in seconds for which this limit is applicable.
        '''
        # Source: https://www.linode.com/api/linode/linode.create
        # As of July 2017, the creation rate limit seems to be 
        # 250 linodes per hour.
        return (250, 3600)
    

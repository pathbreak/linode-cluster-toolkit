import requests

# TODO Eventually use linode-api library. However, as of July 2017, it 
# throws some errors related to its internal imports and is therefore 
# unusable.
#from linode import LinodeClient, LinodeLoginClient, OAuthScopes, Service

class APIService(object):
    '''
    Wrapper for Linode's APIs and SDK.
    
    Uses the v4 API python SDK (https://github.com/linode/python-linode-api) 
    whenever possible, but also uses raw v4 REST requests or v3 API if they're useful
    (for example, as of July 2017, there are no v4 image management APIs while v3 has
    them).
    '''
    
    
    V4_API_URL = 'https://api.linode.com/v4/'
    V3_API_URL = 'https://api.linode.com/


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
        # API service queries secrets service for appropriate API
        # authentication tokens.
        self.tk.secrets_service().initialize(self.tk)
        
        
        self._initialized = True
        
        
    def close(self):
        pass
        
        
    #=============================== FUNCTIONALITY =====================
    
    def create_node(self, tkctx, node_type, region, distribution, root_ssh_key=None):
        '''
        Create a linode.
        
        Arguments:
          tkctx - The ToolkitContext that specifies the app and customer
            scope for this creation operation.
            
          node_type - The type of the linode.
          
          region - Region/datacenter where node should be created
          
          distribution - The OS distribution to install on this node
        '''
        
        # Note: v4 API 'create' does much more than v3 create, but 
        # it does not boot the linode, only creates linode,
        # disks and a config.
        
        v4_token = self._get_v4_token(tkctx)
        if v4_token is None:
            raise AuthenticationError('No v4 API token available in secrets for application {0} customer {1}'.format(
                tkctx.app_id, tkctx.cust_id
            ))
        
        if root_ssh_key is None:
            secrets = self.tk.secrets_service()
            root_ssh_key = secrets.get_default_root_ssh_public_key(tkctx)
            if root_ssh_key is None:
                raise AuthenticationError('No default SSH public key available in secrets for application {0} customer {1}'.format(
                    tkctx.app_id, tkctx.cust_id
                ))
            
        requests.post('')
        
        # If there's no 'root_pass' argument, the library autogenerates a password.
        # If there's no 'root_ssh_key' argument, there won't be SSH key authentication.
        l, passwd = client.linode.create_instance(node_type, region, distribution=distribution, 
            root_ssh_key='/home/karthik/.ssh/id_rsa.pub')
            
            
    #============================ PRIVATE ==============================



    def _get_v4_token(self, tkctx):
        secrets = self.tk.secrets_service()
        
        # If the context has a v4 oauth token, use that.
        v4_oauth_token = secrets.get_v4_oauth_token(tkctx) 
        if v4_oauth_token is not None:
            return v4_oauth_token
        
        # If not, if they have a v4 personal token, use that.
        v4_personal_token = secrets.get_v4_personal_token(tkctx)
        if v4_personal_token is not None:
            return v4_personal_token
            
        return None
        
        
    

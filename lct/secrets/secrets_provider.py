class SecretsProvider(object):
    '''
    Interface to be implemented by a secrets provider.
    '''
    def initialize(self, tk):
        raise NotImplementedError('subclasses should override this')
        
    def close(self):
        raise NotImplementedError('subclasses should override this')
        
    def get_v3_api_key(self, tkctx):
        raise NotImplementedError('subclasses should override this')
        
        
        
    def get_v4_personal_token(self, tkctx):
        raise NotImplementedError('subclasses should override this')
        
        
        
    def get_v4_oauth_token(self, tkctx):
        raise NotImplementedError('subclasses should override this')
        
        
        
    def get_v4_oauth_client_id(self, tkctx):
        raise NotImplementedError('subclasses should override this')
        
        
        
    def get_v4_oauth_client_secret(self, tkctx):
        raise NotImplementedError('subclasses should override this')
        
        
        
    def get_default_root_password(self, tkctx):
        raise NotImplementedError('subclasses should override this')
        
        

    def get_default_root_ssh_public_key(self, tkctx):
        raise NotImplementedError('subclasses should override this')
        
        
        
    def get_node_password(self, tkctx, node, user):
        raise NotImplementedError('subclasses should override this')
        
        
        
    def get_node_ssh_key(self, tkctx, node, user):
        raise NotImplementedError('subclasses should override this')
        
        
    
    def store_v3_api_key(self, tkctx, v3_api_key):
        raise NotImplementedError('subclasses should override this')
        
        
        
    def store_v4_personal_token(self, tkctx, v4_personal_token):
        raise NotImplementedError('subclasses should override this')
        
        
        
    def store_v4_oauth_token(self, tkctx, v4_oauth_token):
        raise NotImplementedError('subclasses should override this')
        
        
        
    def store_v4_oauth_client_id(self, tkctx, v4_oauth_client_id):
        raise NotImplementedError('subclasses should override this')
        
        
        
    def store_v4_oauth_client_secret(self, tkctx, v4_oauth_client_secret):
        raise NotImplementedError('subclasses should override this')
        
        
        
    def store_default_root_password(self, tkctx, default_root_password):
        raise NotImplementedError('subclasses should override this')
        
        

    def store_default_root_ssh_public_key(self, tkctx, default_root_ssh_public_key):
        raise NotImplementedError('subclasses should override this')
        
        
        
    def store_node_password(self, tkctx, node, user, password):
        raise NotImplementedError('subclasses should override this')
        
        
        
    def store_node_ssh_key(self, tkctx, node, user, ssh_key):
        raise NotImplementedError('subclasses should override this')


    

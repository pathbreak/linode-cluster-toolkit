import os
import os.path
from glob import glob

from lct.utils.dpath_utils import dpath_get
from lct.toolkit import ToolkitContext



class SimpleSecretsProvider(object):
    
    '''
    A simple but insecure secrets provider that is useful for simple command line
    tools installed on a personal machine and not shared with others.
    
    It simply stores all secrets in
    a dict in memory, and optionally persists them under configured directory. 
    
    If persistence is enabled, secrets are stored immediately whenever
    a store* function is called. That's useful for
    command line tools that run single commands and terminate.
    Secrets are persisted as files under 
        <persist-path>/ < tkctx.Application ID > / < tkctx.Customer ID>
    
    Toolkit configuration flags used by this provider:
     secrets
       simpleprovider
         persist  => (optional) if 'true', persists secrets. 'false' by default
         persist-path => (optional) if persist is enabled, persist secrets under this
            directory. Default is current directory.
       
    
    TODO:
    * Support optional simple password-based encryption for all secrets.
      Useful for command line clients.
      This class only uses what's in the toolkit configuration, but
      a tool (like linodetool) can convert cmdline arg or env variable
      into a toolkit conf flag.
    '''
    
    V3_API_KEY_SUFFIX = 'v3apikey'
    V4_PERSONAL_TOKEN_SUFFIX = 'v4perstoken'
    V4_OAUTH_TOKEN_SUFFIX = 'v4oauthtoken'
    V4_OAUTH_TOKEN_SUFFIX = 'v4oauthtoken'
    DEFAULT_ROOT_PASSWORD_SUFFIX = 'defaultrootpswd'
    DEFAULT_ROOT_SSH_PUBLIC_SUFFIX = 'defaultpublicssh'
    
    
    def __init__(self):
        self._initialized = False
        self.secrets = {} 


        
    def initialize(self, tk):
        
        if self._initialized:
            return
            
        # If configuration specifies persistence, read all 
        # stored secrets and cache them.
        self._should_persist = bool(dpath_get(tk.conf, 'secrets/simpleprovider/persist', False))
        self._persist_path = dpath_get(tk.conf, 'secrets/simpleprovider/persist-path', './')
        
        if self._should_persist:
            self._load_secrets()
        
        self._initialized = True
        
        
    def close(self):
        pass



    #====================== SecretsProvider interface ==================

    def get_v3_api_key(self, tkctx):
        path = self._make_path(tkctx, self.V3_API_KEY_SUFFIX)
        return self.secrets.get(path, None)
        
        
        
    def get_v4_personal_token(self, tkctx):
        path = self._make_path(tkctx, self.V4_PERSONAL_TOKEN_SUFFIX)
        return self.secrets.get(path, None)
        
        
        
    def get_v4_oauth_token(self, tkctx):
        path = self._make_path(tkctx, self.V4_OAUTH_TOKEN_SUFFIX)
        return self.secrets.get(path, None)
        
        
        
    def get_v4_oauth_client_id(self, tkctx):
        raise NotImplementedError('subclasses should override this')
        
        
        
    def get_v4_oauth_client_secret(self, tkctx):
        raise NotImplementedError('subclasses should override this')
        
        
        
    def get_default_root_password(self, tkctx):
        path = self._make_path(tkctx, self.DEFAULT_ROOT_PASSWORD_SUFFIX)
        return self.secrets.get(path, None)
        
        

    def get_default_root_ssh_public_key(self, tkctx):
        path = self._make_path(tkctx, self.DEFAULT_ROOT_SSH_PUBLIC_SUFFIX)
        return self.secrets.get(path, None)
        
        
        

        
    def get_node_password(self, tkctx, node, user):
        raise NotImplementedError('subclasses should override this')
        
        
        
    def get_node_ssh_key(self, tkctx, node, user):
        raise NotImplementedError('subclasses should override this')

    
        
    def store_v3_api_key(self, tkctx, v3_api_key):
        self._store(tkctx, self.V3_API_KEY_SUFFIX, v3_api_key)
        
        
    def store_v4_personal_token(self, tkctx, v4_personal_token):
        self._store(tkctx, self.V4_PERSONAL_TOKEN_SUFFIX, v4_personal_token)
        
        
    def store_v4_oauth_token(self, tkctx, v4_oauth_token):
        self._store(tkctx, self.V4_OAUTH_TOKEN_SUFFIX, v4_oauth_token)
       
        
        
    def store_v4_oauth_client_id(self, tkctx, v4_oauth_client_id):
        raise NotImplementedError('subclasses should override this')
        
        
        
    def store_v4_oauth_client_secret(self, tkctx, v4_oauth_client_secret):
        raise NotImplementedError('subclasses should override this')
        
        
    def store_default_root_password(self, tkctx, default_root_password):
        self._store(tkctx, self.DEFAULT_ROOT_PASSWORD_SUFFIX, default_root_password)
        
        

    def store_default_root_ssh_public_key(self, tkctx, default_root_ssh_public_key):
        self._store(tkctx, self.DEFAULT_ROOT_SSH_PUBLIC_SUFFIX, default_root_ssh_public_key)
        
        
        

        
    def store_node_password(self, tkctx, node, user):
        raise NotImplementedError('subclasses should override this')
        
        
        
    def store_node_ssh_key(self, tkctx, node, user, ssh_key):
        raise NotImplementedError('subclasses should override this')



    #======================== private methods ==========================


    def _store(self, tkctx, suffix, value):
        path = self._make_path(tkctx, suffix)
        self.secrets[path] = value
        self._persist(path, tkctx, value)



    def _persist(self, path, tkctx, value):
        if not self._should_persist:
            return
            
        dest_dir = os.path.join(
            self._persist_path, 
            tkctx.app_id, 
            tkctx.cust_id)
        
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
            
        suffix = path.split('/')[-1]
        secret_filename = os.path.join(dest_dir, suffix)
        with open(secret_filename, 'w') as secret_file:
            secret_file.write(value)
            
            
    def _load_secrets(self):
        for secret_filename in glob(os.path.join(self._persist_path, '*/*/*')):
            with open(secret_filename, 'r') as secret_file:
                value = secret_file.read()
                
            parts = secret_filename.split('/')
            suffix = parts[-1]
            cust_id = parts[-2]
            app_id = parts[-3]
            
            
            path = self._make_path(ToolkitContext(app_id, cust_id), suffix)
            self.secrets[path] = value


    def _make_path(self, tkctx, suffix):
        return 'secrets/{0}/{1}/{2}'.format(tkctx.app_id, tkctx.cust_id, suffix)

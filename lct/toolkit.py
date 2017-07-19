from .clusters.cluster_service import ClusterService
from .inventory.inventory_service import InventoryService
from .secrets.secrets_service import SecretsService
from .tasks.task_service import TaskService
from .linodeapi.api_service import APIService
from .linodeinfo.linode_info_service import LinodeInfoService

import codecs


class Toolkit(object):
    '''
    A `Toolkit` object is the primary interface of this library.
    It provides access to all other services this library provides.
    
    Generally, a process needs to create only one Toolkit object, unless
    it requires different toolkit configurations for different clusters.
    
    Multiple applications and customers can share the same resources by configuring
    the ToolkitConfiguration appropriately.
    '''
    
    def __init__(self, tk_conf):
        '''
        Create a new Toolkit object which is the primary interface to access
        all services of the toolkit library.
        
        Args:
          tk_conf : dict - A tooklit configuration dict that specifies configuration settings
            for all the services used by and provided by the toolkit.
        '''
        assert tk_conf is not None
        
        self.conf = tk_conf
        
        self._cluster_service = None
        self._api_service = None
        self._linode_info_service = None
        self._inventory_service = None
        self._secrets_service = None
    
    
        
    def initialize(self):
        '''
        Initializes all the other services and implementation providers that
        the toolkit is configured to use.
        '''
        
        # First create all the service objects, and then call their initialization
        # methods. Since every service accesses other services via this Toolkit object,
        # initializing a service immediately after creation means there is a risk 
        # that a required service it depends on hasn't been created yet.
        self._api_service = APIService()
        self._cluster_service = ClusterService()
        self._linode_info_service = LinodeInfoService()
        self._inventory_service = InventoryService()
        self._secrets_service = SecretsService()

        # The order below is kind of common sensical, but not critical for operations
        # because every service anyway makes sure all services it needs are initialized.
        self._api_service.initialize(self)
        self._linode_info_service.initialize(self)
        self._cluster_service.initialize(self)
        self._inventory_service.initialize(self)
        self._secrets_service.initialize(self)
        
    
    
    def close(self):
        '''
        Closes all the other services and implementation providers that
        the toolkit is configured to use.
        '''
        self._cluster_service.close()
        
        self._api_service.close()
        
        self._secrets_service.close()
        
        self._inventory_service.close()
        
        
        
        
        
    def cluster_service(self):
        return self._cluster_service
    
    
    
    def api_service(self):
        return self._api_service
        
        
        
    def secrets_service(self):
        return self._secrets_service
        
    
    def inventory_service(self):
        return self._inventory_service
        

   



        
class ToolkitContext(object):
    '''
    A toolkit context represents the {application, customer} context
    for carrying out a cluster operation. 
    
    A context for every operation is necessary because the toolkit depends 
    on resources like message queues, database tables and secrets namespaces
    which may have to be shared by multiple applications 
    and by multiple customer accounts.
    
    The context enables multiple applications running in different
    processes use the library and share those resources safely
    while keeping their data separate.
    
    The context also enables a single application such as a SaaS cater to multiple
    customer accounts and share resources safely while keeping data of different
    customers separated.
    
    In a SaaS or other multi-customer environment, there should be multiple ToolkitContexts,
    one for each customer.
    '''
    
    def __init__(self, app_id, cust_id):
        self.app_id = app_id
        self.cust_id = cust_id
    
    
    
class ToolkitConfigurationLoader(object):
    '''
    Just a helper to load toolkit configuration dicts from YAML and JSON
    files.
    '''



    @classmethod    
    def load_from_yaml(clz, filename):
        with codecs.open(filename, 'r', encoding="utf-8") as yaml_file:
            conf = yaml.safe_load(yaml_file)
            
        return conf



    @classmethod
    def load_from_json(clz, filename):
        with open(filename, 'r') as json_file:
            conf = json.load(json_file)
            
        return conf
        
    


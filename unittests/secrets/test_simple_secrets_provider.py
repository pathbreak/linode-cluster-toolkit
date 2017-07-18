from __future__ import print_function

import unittest
import os
import tempfile
import shutil
from pprint import pprint


from lct.secrets.simple_secrets_provider import SimpleSecretsProvider
from lct.toolkit import Toolkit, ToolkitContext



class TestSimpleSecretsProvider(unittest.TestCase):
    
    def test_initialize(self):
        temp_dir = tempfile.mkdtemp(prefix='lctunittest-')
        tk_conf = {
            'secrets': {
                'simpleprovider': {
                    'persist' : True,
                    'persist-path': temp_dir
                }
                    
            }
        }
        tk = Toolkit(tk_conf)

        ssp = SimpleSecretsProvider()
        ssp.initialize(tk)
        
        ssp.store_v3_api_key(ToolkitContext('app1', 'cust1'), 'mysecretv3apikey1')
        ssp.store_v4_personal_token(ToolkitContext('app1', 'cust1'), 'mysecretv4pat1')
        
        ssp.store_v3_api_key(ToolkitContext('app1', 'cust2'), 'mysecretv3apikey2')
        ssp.store_v4_personal_token(ToolkitContext('app1', 'cust2'), 'mysecretv4pat2')
        
        ssp.store_v3_api_key(ToolkitContext('app2', 'cust3'), 'mysecretv3apikey3')
        ssp.store_v4_personal_token(ToolkitContext('app2', 'cust3'), 'mysecretv4pat3')
        
        ssp.store_v3_api_key(ToolkitContext('app2', 'cust4'), 'mysecretv3apikey4')
        ssp.store_v4_personal_token(ToolkitContext('app2', 'cust4'), 'mysecretv4pat4')
        
        pprint(ssp.secrets)
        
        # Test that secret stored just now is cached.
        self.assertEqual(ssp.get_v3_api_key(ToolkitContext('app1', 'cust1')), 'mysecretv3apikey1')
        
        # Test that the file is persisted.
        self.assertTrue(os.path.isfile(
            os.path.join(temp_dir, 'app1', 'cust1', SimpleSecretsProvider.V3_API_KEY_SUFFIX )))
        
        
        for p in os.walk(temp_dir):
            print(p)
        
        # Test loading
        ssp2 = SimpleSecretsProvider()
        ssp2.initialize(tk)
        self.assertEqual(ssp.secrets, ssp2.secrets)
        
        shutil.rmtree(temp_dir)
        
   
if __name__ == '__main__':
    unittest.main()

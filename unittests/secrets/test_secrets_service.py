from __future__ import print_function

import unittest

from lct.secrets.secrets_service import SecretsService
from lct.toolkit import Toolkit, ToolkitContext



class TestSecretsService(unittest.TestCase):

    def test_initialize(self):
        tk_conf = {
            
            'secrets': {
                'provider' : 'lct.secrets.simple_secrets_provider.SimpleSecretsProvider',
                
                'simpleprovider': {
                    'persist' : True,
                    'persist-path': '.'
                }
                    
            }
        }
        
        tk = Toolkit(tk_conf)
        s = SecretsService()
        s.initialize(tk)
        self.assertEqual('SimpleSecretsProvider', s.provider().__class__.__name__)
    
if __name__ == '__main__':
    unittest.main()

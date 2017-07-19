'''
linodetool is a command line application that makes it easy to create clusters
of nodes or single nodes on Linode cloud. 

It uses the Linode Cluster Toolkit and most of its services. So it also 
serves as a good demo client for the toolkit.
'''

from __future__ import print_function

import argparse
import os.path

from lct.toolkit import Toolkit, ToolkitContext


# Globals
secret_types = ['api-key', 'personal-token', 'oauth-token', 
    'oauth-client-id', 'oauth-client-secret',
    'default-root-password', 'default-root-ssh-public-key']
secret_store_funcs = ['store_v3_api_key', 'store_v4_personal_token', 'store_v4_oauth_token', 
    'store_v4_oauth_client_id', 'store_v4_oauth_client_secret',
    'store_default_root_password','store_default_root_ssh_public_key']
    
DEFAULT_APP = 'linodetool'
DEFAULT_CUSTOMER = 'me'


def main():
    print('Welcome to the Linode Cluster Tool!')
    
    args, parser = configure_arguments_parser()
    args.func(args)
    
    
def cluster_create(args):
    pass


def cluster_delete(args):
    pass
    
    
def node_create(args):
    
    # Create toolkit object
    # TODO If a toolkit configuration is explicitly specified,
    # load that, otherwise use default.

    tk_conf = default_toolkit_conf()
    tk = Toolkit(tk_conf)
    tk.initialize()
    
    tkctx = ToolkitContext(args.app_id, args.cust_id)
    tk.api_service().create_node()

    

def node_delete(args):
    pass
    
    
def secret_add(args):
    # TODO If a toolkit configuration is explicitly specified,
    # load that, otherwise use default.
    tk_conf = default_toolkit_conf()
    tk = Toolkit(tk_conf)
    tk.initialize()

    secrets = tk.secrets_service().provider()
    
    store_func_name = secret_store_funcs[secret_types.index(args.secret_type)]
    store_func = getattr(secrets, store_func_name)
    
    tkctx = ToolkitContext(args.app_id, args.cust_id)
    
    # If the secret type is ssh public key, assume it's a public key file path
    # and attempt to read from the file.
    if args.secret_type == 'default-root-ssh-public-key':
        is not os.path.isfile(args.secret_value):
            print('Error: Specify a public key file as value')
            return
            
        with open(args.secret_value, 'r') as ssh_key_file:
            args.secret_value = ssh_key_file.read()
        args.secret_value = args.secret_value.replace('\n', '')
    
    store_func(tkctx, args.secret_value)
    print(secrets.secrets)
    print('Secret added')    


    
def default_toolkit_conf():
    default_tk_conf = {
        
        'secrets': {
            'provider' : 'lct.secrets.simple_secrets_provider.SimpleSecretsProvider',
            
            'simpleprovider': {
                'persist' : True,
                'persist-path': os.path.join(os.path.expanduser('~'), '.linodetool', 'secrets')
            }
                
        },
        
        'tasks' : {
            'executor' : 'lct.tasks.immediate_executor.ImmediateExecutor'
        },
        
        'info' : {
            'cache-path' : os.path.join(os.path.expanduser('~'), '.linodetool', 'info'),
            'update-cache' : 1 # update if last update was more than this many days
        }
    }
    
    return default_tk_conf


   
    
def configure_arguments_parser():
    parser = argparse.ArgumentParser()
    
    actions = parser.add_subparsers(dest='cmd', title='commands')

    # Arguments for Cluster Operations:
    cluster_parser = actions.add_parser('cluster', help='Cluster Operations')

    cluster_cmds_parser = cluster_parser.add_subparsers(dest='cluster_cmd', metavar='COMMAND', 
        title='Cluster command')

    cluster_create_parser = cluster_cmds_parser.add_parser('create', help='Create a cluster from a cluster plan')
    
    cluster_create_parser.set_defaults(func = cluster_create)

    cluster_delete_parser = cluster_cmds_parser.add_parser('delete', help='Delete an existing cluster')
    cluster_delete_parser.set_defaults(func = cluster_delete)
    

    # Arguments for Node Operations:
    node_parser = actions.add_parser('node', help='Single Node Operations')

    node_cmds_parser = node_parser.add_subparsers(dest='node_cmd', metavar='COMMAND', 
        title='Node command')
        
    node_create_parser = node_cmds_parser.add_parser('create', help='Create a linode')
    
    node_create_parser.add_argument(dest='node_type', metavar='NODE-TYPE',
        help='Node type for this node. Run "linodetool types" to see list of types')
        
    node_create_parser.add_argument(dest='region', metavar='REGION',
        help='Region/datacenter for this node. Run "linodetool regions" to see list of regions')
        
    node_create_parser.add_argument(dest='distribution', metavar='DISTRIBUTION',
        help='OS Distribution for this node. Run "linodetool distributions" to see list of distributions')
    
    node_create_parser.set_defaults(func = node_create)
        
    node_delete_parser = node_cmds_parser.add_parser('delete', help='Delete a linode')
    node_delete_parser.set_defaults(func = node_delete)
    
    
    # Arguments for Secrets Operations:
    secrets_parser = actions.add_parser('secret', help='Secrets Management')

    secret_cmds_parser = secrets_parser.add_subparsers(dest='secret_cmd', metavar='COMMAND', 
        title='Secrets command')
        
    secret_add_parser = secret_cmds_parser.add_parser('set', help='Set a secret')
    
    secret_add_parser.add_argument(dest='secret_type', metavar='SECRET-TYPE',
        choices = secret_types,
        help='Type of secret. ' + str(secret_types))

    secret_add_parser.add_argument(dest='secret_value', metavar='SECRET-VALUE',
        help='Value of the secret')
    
    secret_add_parser.add_argument(dest='app_id', metavar='APPLICATION-ID', nargs='?',
        default=DEFAULT_APP,
        help='ID of the application that uses this secret. Default is "linodetool"')

    secret_add_parser.add_argument(dest='cust_id', metavar='CUSTOMER-ID', nargs='?',
        default=DEFAULT_CUSTOMER,
        help='ID of the customer this secret belongs to. Default is "me"')

    secret_add_parser.set_defaults(func = secret_add)
    
    args = parser.parse_args()
    return args, parser
    

if __name__ == '__main__':
    main()

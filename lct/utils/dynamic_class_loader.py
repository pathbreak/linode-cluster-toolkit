import importlib

def instantiate(class_name):
    '''
    Dynamically load a given class from its name and instantiate it. 

    '''
    
    # Every type is available via getattr() on a module.
    # So to load a type from a string, first load the module using
    # importlib.import_module, and then look up the type using getattr()
    
    comps = class_name.split('.')
    provider_module_name = '.'.join(comps[:-1])
    provider_class_name = comps[-1]
    
    # This'll raise ImportError if there module name is wrong.
    provider_module = importlib.import_module(provider_module_name)
    
    # This'll raise AttributeError if there's no class of that name in the module.
    provider_class = getattr(provider_module, provider_class_name)
    instance = provider_class()
    
    return instance

    

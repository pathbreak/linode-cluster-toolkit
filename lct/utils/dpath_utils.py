import dpath.util

def dpath_get(obj, glob, default_value, separator="/"):
    '''
    Just a helper to make dpath.util.get easier to use.
    
    A problem with dpath.util.get() is that it throws a KeyError if there is a problem in the
    path, requiring additional boilerplate to handle it. 
    
    This function consumes any KeyError and returns the default value.
    '''
    ret = default_value
    try:
        ret = dpath.util.get(obj, glob, separator)
    except KeyError as k:
        ret = default_value
        
    return ret

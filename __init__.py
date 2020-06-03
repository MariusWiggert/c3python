__all__ = [ 'get_c3' ]
__version__ = '0.1'

def get_c3(url, tenant, tag, mode='thick', define_types=True, auth=None):
    """
    Returns c3remote type system for python.
    """
    try:
        from urllib.request import urlopen
    except ImportError:
        from urllib2 import urlopen
    from types import ModuleType
    c3iot = ModuleType('c3IoT')
    c3iot.__loader__ = c3iot
    src = urlopen(url + '/public/python/c3remote_bootstrap.py').read()
    exec(src, c3iot.__dict__)
    return c3iot.C3RemoteLoader.typeSys(
        url=url,
        tenant=tenant,
        tag=tag,
        mode=mode,
        auth=auth,
        define_types=define_types
    )

'''
This module is used to loader the plugins.
'''
import os
from importlib import import_module


def start(file_list=os.listdir("codeql/plugins/")):
    '''
    load the plugins you want
    '''
    for file in file_list:
        if not file.endswith('.py') or file.startswith('_'):
            continue
        load_plugin(file)


def load_plugin(file):
    '''
    load one plugin
    '''
    plugin_name = os.path.splitext(file)[0]
    import_module("codeql.plugins." + plugin_name).run()

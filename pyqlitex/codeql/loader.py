'''
This module is used to loader the plugins.
'''
import os
import sys
from importlib import import_module
from pathlib import Path
from typing import List

from dotenv import load_dotenv

load_dotenv()
PROJECT_ROOT = os.getenv("PROJECT_ROOT")

print(PROJECT_ROOT)

class CodeQLLoader:
    '''
        Class CodeQLLoader . Used to load plugins.
    '''
    def __init__(self, database_path: str, plugin_dir: Path | None) -> None:
        self.file_list: List[str]
        self.plugin_dir: None | Path = plugin_dir or Path(PROJECT_ROOT) / "pyqlitex" / "codeql" / "plugins"
        self.database_path: Path = Path(database_path)

    def start(self) -> None:
        '''
            start detect plugin dir.
        '''
        sys.path.append(str(self.plugin_dir))
        for file in self.plugin_dir.iterdir():
            if file.suffix == "py" and not file.stem.startswith("_"):
                self.load_plugin(file)

    def load_plugin(self, file: Path) -> None:
        '''
        Load python plugin file as 
        '''
        plugin_name = file.stem
        Plugin = import_module("." + plugin_name).CodeQLPlugin(self.plugin_dir, self.database_path)
        Plugin.start()


# def start(file_list=os.listdir("codeql/plugins/")):
#     '''
#     load the plugins you want
#     '''
#     for file in file_list:
#         if not file.endswith('.py') or file.startswith('_'):
#             continue
#         load_plugin(file)


# def load_plugin(file):
#     '''
#     load one plugin
#     '''
#     plugin_name = os.path.splitext(file)[0]
#     import_module("codeql.plugins." + plugin_name).run()

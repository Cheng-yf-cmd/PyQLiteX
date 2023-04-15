'''
    __init__ of the codeql dir
'''
__all__ = ["InitCodeQL", "CodeQLLoader", "code_wrapper"]
import os

from dotenv import load_dotenv

from .init import InitCodeQL
from .loader import CodeQLLoader

load_dotenv()
PROJECT_ROOT = os.getenv("PROJECT_ROOT")

def code_wrapper(**kwargs) -> None:
    '''
        Wrapper of CodeQL module
    '''
    init_codeql: InitCodeQL = InitCodeQL(kwargs["database_path"], kwargs["project_path"], )
    codeql_loader: CodeQLLoader = CodeQLLoader(plugin_dir=kwargs.get("plugin_dir")
                                               , database_path=kwargs["database_path"], )
    init_codeql.create_database()
    codeql_loader.start()

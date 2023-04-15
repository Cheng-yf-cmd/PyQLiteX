'''
This module is used to query the goal with the QLFiles and database.
'''
import os
import subprocess
from importlib import import_module
from pathlib import Path
from typing import List

from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = os.getenv("PROJECT_ROOT")
PLUGINS_PATH = 'codeql/plugins'

PACK_INTALL = 'codeql pack install'
# QUERY_RUN = 'codeql query run'


class CodeQLPlugin:
    '''
    this class deal with the work about codeql
    '''

    def __init__(self, database_path: Path, plugin_dir: Path) -> None:
        self.qlfile_path: Path = plugin_dir / "QLFile"
        self.qldirs: List[Path] = []
        self.database_path: Path = database_path
        self.output_file: Path = Path(PROJECT_ROOT) / "pyqlitex" / "output" / "sql.txt"

    def find_qlfiles(self) -> None:  # load QL files
        '''
        load settings and find all the QLFiles
        '''
        files = self.qlfile_path.iterdir()

        for file in files:
            if file.is_file():
                continue
            self.qldirs.append(file)

    def query(self, dir_name: Path) -> str:
        '''
        query one QL file
        '''
        # qlpath = self.path + '/' + file_name
        qlfile:Path | None = None
        for file in dir_name.iterdir():
            if file.suffix("ql"):
                qlfile = file
                break

        subprocess.run(PACK_INTALL, cwd=dir_name, check=False, shell=True)
        subprocess.run(
            [
                'codeql',
                'query',
                'run',
                str(qlfile),
                '-d=' + self.database_path,
            ],
            shell=True,
            check=False,
            stdout=open(self.output_file, 'w', encoding='UTF-8'),
        )
        parser = import_module('codeql.plugins.QLFile.' + dir_name.stem + '.parser')
        with open(self.output_file, 'r', encoding='UTF-8') as f:
            return parser.parse(f.read())

    def start(self):
        '''
        give one database, query all the QL files, and return result
        '''
        self.find_qlfiles()
        result = []
        for qlfile in self.qldirs:
            result.append(self.query(qlfile))
        return result


# def run():
#     '''
#     execute the codeql class
#     '''
#     CodeqlDefault().start()

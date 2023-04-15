'''
This module is used to query the goal with the QLFiles and database.
'''
import json
import os
import subprocess
from importlib import import_module
from pathlib import Path

PROJECT_ROOT = Path.cwd()
PLUGINS_PATH = 'codeql/plugins'

PACK_INTALL = 'codeql pack install'
# QUERY_RUN = 'codeql query run'


class CodeqlDefault:
    '''
    this class deal with the work about codeql
    '''

    def __init__(self):
        self.path = ''
        self.qlfiles = []
        self.settings = {}

    def init(self):  # load QL files
        '''
        load settings and find all the QLFiles
        '''
        self.path = './codeql/plugins/QLFile'
        files = os.listdir(self.path)
        self.qlfiles = []
        self.settings = json.loads(
            open('../settings.json', 'r', encoding='UTF-8').read()
        )

        for file in files:
            if os.path.isfile(self.path + '/' + file):
                continue
            self.qlfiles.append(file)

    def query(self, file_name):
        '''
        query one QL file
        '''
        qlpath = self.path + '/' + file_name
        ql_name = ''
        for file in os.listdir(qlpath):
            if file.endswith('.ql'):
                ql_name = file
                break
        current_path = PROJECT_ROOT / PLUGINS_PATH / 'QLFile' / file_name

        subprocess.run(PACK_INTALL, cwd=current_path, check=False, shell=True)
        subprocess.run(
            [
                'codeql',
                'query',
                'run',
                current_path / ql_name,
                '-d=' + self.settings['DatabasePath'],
            ],
            shell=True,
            check=False,
            stdout=open('./output/sql.txt', 'w', encoding='UTF-8'),
        )
        parser = import_module('codeql.plugins.QLFile.' + file_name + '.parser')
        sql = open('./output/sql.txt', 'r', encoding='UTF-8').read()
        return parser.parse(sql)

    def start(self):
        '''
        give one database, query all the QL files, and return result
        '''
        self.init()
        result = []
        for qlfile in self.qlfiles:
            result.append(self.query(qlfile))
        return result


def run():
    '''
    execute the codeql class
    '''
    CodeqlDefault().start()

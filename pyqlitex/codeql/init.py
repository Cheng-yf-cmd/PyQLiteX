'''
The _init class is used to initialize the codeql database now.
'''
import json
import subprocess


class _init:
    def __init__(self):
        self.databasepath = ''
        self.projectpath = ''
        self.settings = {}

    def init(self):
        '''
        initialize the project information
        '''
        self.settings = json.loads(
            open('../settings.json', 'r', encoding='UTF-8').read()
        )

        self.databasepath = self.settings['DatabasePath']
        self.projectpath = self.settings['ProjectPath']

    def start(self):
        '''
        create the database for codeql
        '''
        self.init()
        subprocess.run(
            [
                'codeql',
                'database',
                'create',
                self.databasepath,
                '--language=python',
                "--source-root=" + self.projectpath,
                '--overwrite',
            ],
            shell=True,
            check=False,
        )


def run():
    '''
    execute the prework class
    '''
    _init().start()

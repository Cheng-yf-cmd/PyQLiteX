'''
The _init class is used to initialize the codeql database now.
'''
import json
import os
import subprocess
from pathlib import Path
from typing import Dict

from dotenv import load_dotenv

load_dotenv()
PROJECT_ROOT = os.getenv("PROJECT_ROOT")

class InitCodeQL:
    '''
        # ! Wait to be done.
    '''
    def __init__(self, database_path: str | None = None, project_path: str | None= None):
        print("init project")
        self.database_path: str | None = database_path
        self.project_path: str | None = project_path
        self.settings: Dict = {}
        self.init_path()


    def init_path(self):
        '''
        initialize the project information
        '''
        self.settings = json.loads(
           (Path(PROJECT_ROOT) / "settings.json").read_text()
        )

        self.database_path = self.database_path or self.settings['database_path']
        self.project_path = self.project_path or self.settings['project_path']
        print(self.database_path, self.project_path)

    def create_database(self):
        '''
        create the database for codeql
        '''
        # print("___________")
        # print(os.path.join(
        #         'codeql',
        #         'database',
        #         'create',
        #         self.database_path,
        #         '--language=python',
        #         "--source-root=" + self.project_path, # TO-DO: When there's space in path.
        #         '--overwrite',
        #     ))
        # print("___________")
        print("codeql database create " + self.database_path + " --language=Python --source-root=" + self.project_path + " --overwrite",)
        subprocess.run(
            # [
            #     'codeql',
            #     'database',
            #     'create',
            #     # self.database_path.replace(' ', '\\ '),
            #     # '--language=python',
            #     # "--source-root=" + self.project_path.replace(' ', '\\ '), # TO-DO: When there's space in path.
            #     # '--overwrite',
            # ],
            "codeql database create " + self.database_path + " --language=Python --source-root=" + self.project_path + " --overwrite",
            shell=True,
            check=False,
        )


# def run():
#     '''
#     execute the prework class
#     '''
#     _init().start()

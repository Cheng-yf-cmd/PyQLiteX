import os
import json
import subprocess

class _init:
    def init(self):
        self.settings = json.loads(open('../settings.json','r').read())

        self.databasepath = self.settings['DatabasePath']
        self.projectpath = self.settings['ProjectPath']
    
    def start(self):
        self.init()
        # print('codeql database create \"' + self.databasepath + '\" --language=python ' + "--source-root=\"" + self.projectpath + '\" --overwrite')
        subprocess.run(['codeql','database','create',
                       self.databasepath,
                       '--language=python',
                       "--source-root="+self.projectpath,
                       '--overwrite'])
        # os.system('codeql database create \"' + self.databasepath + 
        # '\" --language=python ' + "--source-root=\"" + self.projectpath + '\" --overwrite')

def run():
    _init().start()
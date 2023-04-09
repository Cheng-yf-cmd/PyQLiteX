import os
import json
import subprocess
from pathlib import Path

# PROJECT_ROOT = 
PLUGINS_PATH = 'codeql/plugins'

PACK_INTALL = 'codeql pack install'
QUERY_RUN = 'codeql query run'

class codeql_default:
    def init(self): # load QL files
        self.path = './plugins/QLFile'
        files = os.listdir(self.path)
        self.qlfiles = []
        self.settings = json.loads(open('../settings.json','r').read())

        for f in files:
            if os.path.isfile(self.path+'/'+f):
                continue
            self.qlfiles.append(f)

    def analyze(self, fileName):
        qlpath = self.path + '/' + fileName
        li = os.listdir(qlpath)
        qlName = ''
        for f in li:
            if f.endswith('.ql'):
                qlName = f
                break
        # print('cd ' + qlpath + ' && ls && codeql pack install')
        CURRENT_PATH = PROJECT_ROOT / PLUGINS_PATH
        QL_PATH = CURRENT_PATH / 'QLFile' / fileName / qlName

        subprocess.run(PACK_INTALL,cwd = CURRENT_PATH)
        # os.system('cd ' + qlpath + ' && codeql pack install')
        subprocess.run([QUERY_RUN, QL_PATH, '-d=' + self.settings['DatabasePath']],
                       stdout = open('../output/sql.txt','w'))
        # os.system('codeql query run ' + qlpath + '/' + qlName
        #           + ' -d=\"' + self.settings['DatabasePath']
        #           + '\" > \"../output/sql.txt\"')
        # print('plugins.QLFile.' + fileName +'.parser')
        parser = __import__('plugins.QLFile.' + fileName +'.parser', fromlist = ['QLFile', fileName, 'parser'])
        sql = open('../output/sql.txt','r').read()
        return parser.parse(sql)

    def start(self):
        self.init()
        result = []
        for qlfile in self.qlfiles:
           result.append(self.analyze(qlfile))
        return result

    def stop(self):
        pass

def run():
    codeql_default().start()
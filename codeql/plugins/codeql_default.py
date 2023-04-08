import os
import json

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
        os.system('cd ' + qlpath + ' && codeql pack install')
        os.system('codeql query run ' + qlpath + '/' + qlName
                  + ' -d=\"' + self.settings['DatabasePath']
                  + '\" > \"../output/sql.txt\"')
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
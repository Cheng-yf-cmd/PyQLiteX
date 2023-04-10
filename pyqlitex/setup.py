'''
Setup the project. Which include:
* 
'''
import codeql.basic_info.main as BasicInfo
import codeql.loader as Loader
import codeql.init as Init
from pathlib import Path

def analyze():
    Init.run()
    Loader.Start()

# analyze()

'''

Database = Init(Projecct_Dir)

Loader.Start(Database)
BasicInfo.Start(Database)
'''

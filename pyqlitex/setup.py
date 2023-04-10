'''
Setup the project. Which include:
* 
'''
from pathlib import Path
import codeql.basic_info.main as BasicInfo
import codeql.loader as Loader
import codeql.init as Init


def analyze():
    Init.run()
    Loader.start()


# analyze()

'''

Database = Init(Projecct_Dir)

Loader.Start(Database)
BasicInfo.Start(Database)
'''

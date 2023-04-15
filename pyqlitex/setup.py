'''
Setup the project. Which include:
* 
'''
# import pyqlitex.codeql.basic
import pyqlitex.codeql.init as Init
import pyqlitex.codeql.loader as Loader


def analyze():
    Init.run()
    Loader.start()


# analyze()

'''

Database = Init(Projecct_Dir)

Loader.Start(Database)
BasicInfo.Start(Database)
'''

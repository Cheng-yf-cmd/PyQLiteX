#!/usr/bin/env python
'''
Entry point for project PyQLiteX
'''
import os
import json
import logging

from dotenv import set_key

set_key(".env", "PROJECT_ROOT", os.getcwd())
# set_key(".env", "PROJECT_ROOT", os.getcwd())
set_key(".env", "OUTPUT_DIR", "output")
set_key(".env", "OUTPUT_JSON_NAME", "demo.json")
logging.info("Key in .env set. ")

from pyqlitex.codeql import code_wrapper
from pyqlitex.basic import basic_info

def main():
    '''
    Entry function
    '''
    # logging.info = print
    settings = json.loads(open("settings.json", "r", encoding="utf-8").read())
    code_wrapper(database_path=settings["DatabasePath"], project_path=settings["ProjectPath"], )
    basic_info(work_dir=settings["ProjectPath"])

    # OUTPUT_JSON_NAME = os.getenv("OUTPUT_JSON_NAME") # demo.json

if __name__ == "__main__":
    main()

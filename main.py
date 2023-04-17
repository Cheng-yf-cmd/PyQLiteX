#!/usr/bin/env python
'''
Entry point for project PyQLiteX
'''
import os
import json
import logging
import platform
import http.server
import socketserver
import subprocess

from dotenv import set_key

set_key(".env", "PROJECT_ROOT", os.getcwd())
# set_key(".env", "PROJECT_ROOT", os.getcwd())
set_key(".env", "OUTPUT_DIR", "output")
set_key(".env", "OUTPUT_JSON_NAME", "demo.json")
logging.info("Key in .env set. ")

from pyqlitex.codeql import codeql_wrapper
from pyqlitex.basic import basicinfo_wrapper

def main():
    '''
    Entry function
    '''
    # logging.info = print
    with open("settings.json", "r", encoding="utf-8") as f:
        settings = json.loads(f.read())
    codeql_wrapper(database_path=settings["DatabasePath"], project_path=settings["ProjectPath"], )
    basicinfo_wrapper(work_dir=settings["ProjectPath"])

    class Handler(http.server.SimpleHTTPRequestHandler):
        ''' Customiszed Handler. Use to redirect the displaying directory'''
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, directory="WebUI/", **kwargs)

    with socketserver.TCPServer(("", settings["WebServerPort"]), Handler) as httpd:
        print(f'Listening at http://127.0.0.1:{settings["WebServerPort"]}')
        if platform.system() == "Linux":
            subprocess.run(["xdg-open", f'http://127.0.0.1:{settings["WebServerPort"]}']
                           , check=True)
        if platform.system() == "Windows":
            subprocess.run(["start", f'http://127.0.0.1:{settings["WebServerPort"]}']
                           , check=True)
        httpd.serve_forever()

    # OUTPUT_JSON_NAME = os.getenv("OUTPUT_JSON_NAME") # demo.json

if __name__ == "__main__":
    main()

'''
Use PyTest to Test basic/project.py
'''
import sys
import os
import importlib

sys.path.append(os.path.abspath("../.."))
# TODO: Need to convert to ABSOLUTE path. Commented by Tiger1218<tiger1218.com>
tmp_module = importlib.import_module("CodeQL-based-Python-source-code-scanner")
PythonProject = tmp_module.PythonProject

class TestPythonProject(PythonProject):
    def __init__(self):
        pass
    
    def test_load_from_git(self):
        assert True
    
    def test__parse_pyproject_toml(self):
        assert not self._parse_pyproject_toml
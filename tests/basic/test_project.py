'''
Use PyTest to Test basic/project.py
'''
import sys
import os
import importlib
import pytest

sys.path.append(os.path.abspath("../.."))
print(os.path.abspath("../.."))
# TODO: Need to convert to ABSOLUTE path. Commented by Tiger1218<tiger1218.com>
tmp_module = importlib.import_module("pyqlitex")
from 
PythonProject = tmp_module.PythonProject

class TestPythonProject:
    '''
    Test the class PythonProject in basic/project.py
    '''
    def __init__(self):
        pass

    @pytest.mark.skip(reason="Not finish yet")
    @pytest.mark.unfinish
    def test_load_from_git(self):
        assert True

    def test__parse_pyproject_toml(self):
        assert not self._parse_pyproject_toml
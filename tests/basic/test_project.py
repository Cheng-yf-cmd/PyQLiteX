'''
Use PyTest to Test basic/project.py
'''
import importlib
import os
import sys
from pathlib import Path

import fastentrypoints
import pytest

sys.path.append(os.path.abspath("../.."))
print(os.path.abspath("../.."))
# TODO: Need to convert to ABSOLUTE path. Commented by Tiger1218<tiger1218.com>
tmp_module = importlib.import_module("pyqlitex")
PythonProject = tmp_module.PythonProject

class TestPythonProject:
    '''
    Test the class PythonProject in basic/project.py
    '''
    @pytest.mark.skip(reason="Not finish yet")
    def test_load_from_git(self):
        assert True

    @pytest.mark.parametrize('path',
                             ["/home/tiger1218/dachuang/testsrepo/manim",
                              "/home/tiger1218/dachuang/CVEs/CVE-2022-36069"])
    def test__parse_pyproject_toml(self, path):
        '''
        A unit test for method _parse_pyproject_toml in class `PythonProject`
        '''
        test_project = PythonProject()
        test_project.workdir = Path(path)
        test_project.analyze_dir()
        # test_project.dump_data()
        for metadata in test_project.key:
            assert test_project.key[metadata]

    @pytest.mark.parametrize('path',
                             ["/home/tiger1218/dachuang/testsrepo/flask",
                             "/home/tiger1218/dachuang/testsrepo/django"])
    def test__parse_setup_cfg(self, path):
        '''
        A unit test for method _parse_setup_cfg in class `PythonProject`
        '''
        test_project = PythonProject()
        test_project.workdir = Path(path)
        test_project.analyze_dir()
        for metadata in test_project.key:
            assert test_project.key[metadata]

    @pytest.mark.parametrize('path',
                             ["/home/tiger1218/dachuang/testsrepo/thefuck"])
    def test__parse_setup_py(self, path):
        '''
        A unit test for method _parse_setup_cfg in class `PythonProject`
        '''
        test_project = PythonProject()
        test_project.workdir = Path(path)
        test_project.analyze_dir()
        for metadata in test_project.key:
            assert test_project.key[metadata]

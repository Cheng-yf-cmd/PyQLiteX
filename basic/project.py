import subprocess
import os
from pathlib import Path
import urllib3 
import configparser
import toml
# from 
PROJECT_ROOT = "/home/tiger1218/dachuang/CodeQL-based-Python-source-code-scanner"
OUTPUT_DIR = "output"
PYPI_MIRROR = "https://pypi.org/project/"

GIT_CLONE = "git clone"

class MetadataNotFoundError(Exception):
    def __init__(self, file_type, key):
        self.file_type = file_type
        self.key = key
    
    def __str__(self):
        return f"In file {self.file_type} found not key {self.key}"

class Project:
    def __init__(self):
        self.workdir: Path

        pass

    def load_from_git(self, repo_addr):
        self.method = "git"
        self.remote_repo = repo_addr
        self.name = self._parse_remote_repo(repo_addr)

        # os.chdir(Path(PROJECT_ROOT) / OUTPUT_DIR)
        # if repo
        subprocess.run([GIT_CLONE, repo_addr], shell = True, cwd = Path(PROJECT_ROOT) / OUTPUT_DIR)
        # os.chdir(self.name)
        self.workdir = Path(PROJECT_ROOT) / OUTPUT_DIR / self.name

    def load_from_pypi(self, pypi_name):
        self.method = "pypi"
        self.remote_repo = PYPI_MIRROR
        self.name = pypi_name

        # os.chdir(Path(PROJECT_ROOT) / OUTPUT_DIR)
        # if repo
        # subprocess.run([GIT_CLONE, repo_addr], shell=True)

        os.chdir(self.name)
        self.workdir = Path(PROJECT_ROOT) / OUTPUT_DIR / self.name
    

    def analyze_dir(self):
        flag = 0
        if (self.workdir / "setup.cfg").exists():
            flag = 1
            rets = self._parse_setup_cfg(self.workdir / "setup.cfg")
        
        if(self.workdir / "pyproject.toml").exists():
            flag = 1
            rets = self._parse_pyproject_toml(self.workdir / "pyproject.toml")
        
        if not flag:
            raise FileNotFoundError("Cannot locate file indicates project's metadata.")

        self.pyname, self.author, self.description, self.python_dep = rets


    # @staticmethod
    def _parse_setup_cfg(self, cfg_path):
        rets = []
        metadata_list = ["name", "author", "description", "license"]
        config = configparser.ConfigParser()
        config.read(cfg_path)
        if not "metadata" in config:
            raise MetadataNotFoundError("setup.cfg", "metadata")
        
        for metadata in metadata_list:
            if not metadata in config['metadata']:
                raise MetadataNotFoundError("setup.cfg", metadata)
            rets.append(config['metadata'][metadata])
        
        return rets
    
    @staticmethod
    def _parse_pyproject_toml(self, toml_path):
        rets = []
        toml_config = toml.load(toml_path)
        if "tool" in toml_config and "poetry" in toml_config["tool"]:
            metadata_list = ["name", "authors", "description", "license"]
            for metadata in metadata_list:
                if not metadata in toml_config['tool']['poetry']:
                    raise MetadataNotFoundError("pyproject.toml", metadata)
                rets.append(toml_config['tool']['poetry'][metadata])
        return rets
        

    def output(self):
        for key in dir(self):
            print(f"key {key} exist", end = '')
            if callable(key):
                continue
            print(f" ,value is {dir(self)[key]}")

    @staticmethod
    def _parse_remote_repo(repo_addr):
        parser = urllib3.util.parse_url(repo_addr)
        return parser.path.split('/')[-1]
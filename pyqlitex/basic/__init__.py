'''
# TODO: to be construct, commented by Tiger1218<tiger1218@foxmail.com>
'''
__all__ = ["PythonProject", "MetadataNotFoundError"]
from .exception import MetadataNotFoundError
from .project import PythonProject

def basicinfo_wrapper(work_dir = None):
    python_project = PythonProject(work_dir=work_dir)
    python_project.analyze_dir()
    python_project.dump_data()
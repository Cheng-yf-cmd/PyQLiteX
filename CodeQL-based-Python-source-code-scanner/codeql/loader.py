import os
import subprocess
from importlib import import_module

def Start(file_list = os.listdir("codeql/plugins/")):
	for file in file_list:
		if not file.endswith('.py') or file.startswith('_'):
			continue
		load_plugin(file)

def load_plugin(file):
	pluginName = os.path.splitext(file)[0]
	# sys.path += PROJECT_ROOT / "codeql" / "plugins/"
	import_module("codeql.plugins."+pluginName).run()

# __import__('init').run()
# Start()
import os

def Start(file_list = os.listdir("plugins/")):
	for file in file_list:
		if not file.endswith('.py') or file.startswith('_'):
			continue
		load_plugin(file)

def load_plugin(file):
	pluginName = os.path.splitext(file)[0]
	__import__("plugins."+pluginName, fromlist = [pluginName]).run()

Start()
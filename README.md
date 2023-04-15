# PyQLiteX: A Powerful and Lightweight Python Code Quality and Security Analysis Tool with CodeQL

PyQLiteX is a powerful and lightweight tool for Python code quality and security analysis based on CodeQL. It allows you to input Python project from GitHub Repo or existed python project distributed on PYPI, and automatically parses the basic information of the project and runs the QL file. PyQLiteX also parses the output of CodeQL and displays it in a user-friendly frontend developed by Bootstrap.js.

## Dependencies

### CodeQL

To use this repo, you need to install [CodeQL](https://docs.github.com/en/code-security/codeql-cli/using-the-codeql-cli/getting-started-with-the-codeql-cli#setting-up-the-codeql-cli). Check the installation is successful by running this command in your terminal:

```bash
codeql --version
```

If it appears something like `CodeQL command-line toolchain release 2.11.6.`, the installation succeeds.

If it appears something like `Command not found.`, remember to add the path of binary to the system PATH.

#### ArchLinux

You can install it on ArchLinux only using [AUR](https://aur.archlinux.org/).

```bash
yay -S codeql
```

### Python packages

```bash
pip install -r requirements.txt
```

## For dev-engineer

### Control the Project

We use [poetry](https://python-poetry.org/) to control the whole project. For developing the backend, you need to git clone this repo and cd to its dir, and do following thing:

```bash
poetry install --with dev --sync
poetry shell
# and for some need you want to run some file...
poetry run [filename]
# for more information see the doc.
```

### Python Unit Test

We use [pytest](https://docs.pytest.org/en/7.3.x/) to do the testing work. 

For easiest use, we can just type `pytest` and let it run auto for us.

```bash
pytest
```
You'd better write the test unit.

### Git & GitHub

For git, there's a half official guide called [Progit](https://www.progit.cn/). And see [GitHub Official Guide](https://docs.github.com/zh/get-started) for a deeper understand of GitHub.

### Python Code Style

See [My Note About PEP-8] and install the [pylint] package.

```
.
├── LICENSE
├── README.md
├── basic
│   ├── main.py
│   └── project.py
├── codeql
│   ├── init.py
│   ├── loader.py
│   └── plugins
│       ├── QLFile
│       │   └── QL1
│       │       ├── parser.py
│       │       ├── qlpack.yml
│       │       ├── queries.xml
│       │       └── query.ql
│       ├── __pycache__
│       │   └── codeql_default.cpython-38.pyc
│       └── codeql_default.py
├── main.py
├── output
│   ├── cves.json
│   └── sql.txt
├── requirements.txt
├── settings.json
├── setup.py
└── test.py
```

* The structure of the project maybe not the latest version. (version 083cebb)
* Remember to write the type-hint and docstring. 
* No tester nor project controller yet. 
* Post an issue and AT(@) if you have problem involve someone else.

## Next step for our Project

### Create a benchmark

### Other software

* [Pyre](https://github.com/facebook/pyre-check)
* [bandit](https://github.com/PyCQA/bandit)
* [safety](https://github.com/pyupio/safety)


# {
#   "window.zoomLevel": 1,
#   "workbench.startupEditor": "none",
#   "explorer.compactFolders": false,
#   "editor.fontSize": 26,
#   "terminal.integrated.fontSize": 24,
#   "editor.rulers": [80, 120],
#   "workbench.colorTheme": "OM Theme (Default Dracula Italic)",
#   "workbench.iconTheme": "material-icon-theme",
#   "code-runner.executorMap": {
#     "python": "clear ; python -u"
#   },
#   "code-runner.runInTerminal": true,
#   "code-runner.ignoreSelection": true,
#   "editor.fontFamily": "Consolas, 'Dank Mono', 'Source Code Pro', 'Fira Code', Menlo, 'Inconsolata', 'Droid Sans Mono', 'DejaVu Sans Mono', 'Ubuntu Mono', 'Courier New', Courier, Monaco, monospace",
#   "terminal.integrated.fontFamily": "",
#   "[python]": {
#     "editor.defaultFormatter": "ms-python.python",
#     "editor.tabSize": 4,
#     "editor.insertSpaces": false,
#     "editor.formatOnSave": true
#     // "editor.codeActionsOnSave": {
#     //   "source.fixAll": true,
#     //   "source.fixAll.unusedImports": false,
#     //   "source.organizeImports": true
#     // }
#   },
#   "python.languageServer": "Pylance",
#   "python.formatting.autopep8Args": [
#     "--indent-size=4",
#     "--max-line-length=80"
#     // "--ignore=E111"
#   ],
#   "python.linting.flake8Args": [
#     // "--ignore=E111",
#   ],
#   "python.linting.flake8Enabled": false,
#   "python.linting.mypyEnabled": false,
#   "python.testing.unittestEnabled": false,
#   "python.testing.pytestEnabled": false,
#   "python.analysis.diagnosticSeverityOverrides": {},
#   // "python.defaultInterpreterPath": "./venv/bin/python",
#   "python.analysis.typeCheckingMode": "off",
#   "cSpell.enabled": false
# }
# # from sys import path

# # import aula99_package.modulo
# # from aula99_package import modulo
# # from aula99_package.modulo import *

# # # from aula99_package.modulo import soma_do_modulo

# # # print(*path, sep='\n')
# # print(soma_do_modulo(1, 2))
# # print(aula99_package.modulo.soma_do_modulo(1, 2))
# # print(modulo.soma_do_modulo(1, 2))
# # print(variavel)
# # print(nova_variavel)
# from aula99_package.modulo import fala_oi, soma_do_modulo

# print(__name__)
# fala_oi()
# # __all__ = [
# #     'variavel',
# #     'soma_do_modulo',
# #     'nova_variavel',
# # ]
# from aula99_package.modulo_b import fala_oi

# variavel = 'Alguma coisa'


# def soma_do_modulo(x, y):
#     return x + y


# nova_variavel = 'OK'
# # fala_oi()

# def fala_oi():
#     print('oi')
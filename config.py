import sys
import os
import platform

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

if platform.system() == 'Windows': 
    PYTHON_PATH = os.path.join(PROJECT_ROOT, 'venv_win', 'Lib', 'site-packages')
else:
    PYTHON_PATH = os.path.join(PROJECT_ROOT, 'venv', 'lib', 'python3.12', 'site-packages')

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
if PYTHON_PATH not in sys.path:
    sys.path.insert(0, PYTHON_PATH)

import os
import subprocess
import sys

# This script initializes the environment for CDM8 ASM build/run/debug scripts
# Namely, venv, file pointing to it, and config

venvdir = "cdm8venv"
cfg_filename = 'cdm8config.yml'

if sys.platform == 'win32' or sys.platform == 'cygwin':
    local_venv_loc = "Scripts"
else:
    local_venv_loc = 'bin'

subprocess.call(['python', '-m', 'venv', f'{venvdir}'])
subprocess.call([f'{venvdir}/{local_venv_loc}/pip', 'install', 'pyyaml'])
subprocess.call([f'{venvdir}/{local_venv_loc}/python', 'create_config.py', f'{venvdir}', f'{cfg_filename}'])

with open("VENV_LOCATION", "w") as file:
    file.write(f"{os.getcwd()}/{venvdir}/bin/python")

import sys
import yaml
import argparse as ap
import os


def main():
    parser = ap.ArgumentParser()
    parser.add_argument("venvpath")
    parser.add_argument("config_filename")
    args = parser.parse_args()

    cwd = os.getcwd()

    if sys.platform == 'win32' or sys.platform == 'cygwin':
        local_venv_loc = "Scripts"
    else:
        local_venv_loc = 'bin'

    main_script_location = f'{cwd}/cdm8_asm_brd_script.py'

    cfg = {
        'build': [
            {
                'python_file': f'{main_script_location}',
                'name': 'CDM8 ASM project',
                'entry_point': '',
                'ext': 'asm'
            }
        ],
        'run': [
            {
                'python_file': f'{main_script_location}',
                'name': 'CDM8 ASM project',
                'entry_point': '',
                'ext': 'img'
            }
        ],
        'debug': [
            {
                'python_file': f'{main_script_location}',
                'name': 'CDM8 ASM project',
                'entry_point': '',
                'ext': 'asm'
            }
        ]
    }
    with open(args.config_filename, 'w') as file:
        yaml.dump(cfg, file, default_style='"')
    with open(args.config_filename, 'r') as file:
        print(yaml.load(file, yaml.Loader))


if __name__ == '__main__':
    main()

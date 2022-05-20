from re import sub
import subprocess
import argparse
import pathlib
import os
import functools


def main():
    parser = argparse.ArgumentParser(description='CDM8 build|run|debug script')
    parser.add_argument('-f', '--flag', type=str, choices=['run', 'build', 'debug'],
                        help='execution flag: "build", "run", or "debug" ', )
    parser.add_argument('-n', '--name', type=str, help='name of the project', required=True)
    parser.add_argument('-d', '--project_dir', type=str, help='root directory of the project', required=True)
    parser.add_argument('-p', '--file', nargs="+", help='files in project (first one is main)', required=True)
    parser.add_argument('-e', '--entry_point', help='entry-point of project', required=True)
    parser.add_argument('-ext', '--change_extension', help='changing extension of source files (ex. from ".c" to ".o")')
    parser.add_argument('-b', '--breakpoints', help='breakpoints in project', required=False)

    args = parser.parse_args()

    python_bin = ""

    script_loc = pathlib.Path(__file__).parent.resolve()

    try:
        with open(f"{script_loc}/VENV_LOCATION") as file:
            python_bin = file.read(-1)
    except IOError:
        python_bin = "python"

    if python_bin == "":
        python_bin = "python"

    if args.flag == "build":
        subprocess.call([f"{python_bin}",
                  f"{script_loc}/cdm8_asm_build.py",
                  *(args.file),
                  f"-b", f"{args.breakpoints}",
                  f"-o", f"{args.project_dir}/build/debug.cdm8dbg.yaml",
                  f"-m", f"{script_loc}/standard.mlb"])

    elif args.flag == 'run':
        main_asm_file = args.file[0]
        if main_asm_file[-4:] == '.asm':
            main_asm_file = main_asm_file[:-4] + '.img'
        subprocess.call([f"{python_bin}", f"{script_loc}/cdm8_emu_main.py", f"{main_asm_file}"])

    elif args.flag == 'debug':
        main_asm_file = args.file[0]
        if main_asm_file[:4] == '.asm':
            main_asm_file = main_asm_file[:4] + '.img'
        os.execvp(python_bin, [python_bin, f'{script_loc}/cdm8_emu_debug.py', main_asm_file, '-y', f'{args.project_dir}/build/debug.cd8dbg.yaml'])


if __name__ == '__main__':
    main()
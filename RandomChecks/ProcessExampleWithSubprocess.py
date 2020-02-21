import subprocess
import sys
from locale import format_string


def exec_long_running_proc(command, args):
    cmd = "{} {}".format(command, " ".join(str(arg) if ' ' not in arg else arg.replace(' ','\ ') for arg in args))
    print(cmd)
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # Poll process for new output until finished
    while True:
        nextline = process.stdout.readline().decode('UTF-8')
        if nextline == '' and process.poll() is not None:
            break
        sys.stdout.write(nextline)
        sys.stdout.flush()


    output = process.communicate()[0]
    str = input("Provide the process name: ")
    exitCode = process.returncode

    if (exitCode == 0):
        return output
    else:
        raise Exception(command, exitCode, output)
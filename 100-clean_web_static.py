#!/usr/bin/python3
import os
from fabric.api import lcd, run, local

env.hosts = ['54.146.94.114', '54.172.58.174']


def do_clean(number=0):
    """
    Removes out-of-date archives
    Args:
        number (int): The number of archives to leave.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]

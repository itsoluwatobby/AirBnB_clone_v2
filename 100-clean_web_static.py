#!/usr/bin/python3
import os
from fabric.api import *

env.hosts = ['54.146.94.114', '54.172.58.174']


def do_clean(number=0):
    """
    Removes out-of-date archives
    Args:
        number (int): The number of archives to leave.
    """
    number = 1 if int(number) == 0 else int(number)

    archives_list = sorted(os.listdir("versions"))
    [archives_list.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives_list]

    with cd("/data/web_static/releases"):
        archives_slice = run("ls -tr").split()
        archives = [a for a in archives_slice if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]

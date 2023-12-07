#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the
contents of the web_static folder of your AirBnB Clone
repo, using the function do_pack.
"""
from fabric.api import local
import os
import time


def do_pack():
    """
    A function that generates a .tgx archive from web_static folder
    """
    if not os.path.exist('versions'):
        os.makedirs('versions')

    filename = time.strftime("%Y%m%d%H%M%S")
    filepath = "versions/web_static_{}.tgz".format(filename)

    try:
        local("tar -czvf {} web_static".format(filepath))
        return filepath
    except Exception:
        return None

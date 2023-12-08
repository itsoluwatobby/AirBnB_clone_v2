#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the
contents of the web_static folder of your AirBnB Clone
repo, using the function do_pack.
"""
from fabric.api import local
from time import strftime
from datetime import date


def do_pack():
    """
    A function that generates a .tgx archive from web_static folder
    """
    filename = time.strftime("%Y%m%d%H%M%S")

    try:
        path = "versions/web_static_{}.tgz".format(filename)
        local("mkdir -p versions")
        local("tar -czvf {} web_static/".format(path))
        
        return path
    except Exception as e:
        return None

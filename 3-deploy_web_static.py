#!/usr/bin/python3
"""
a Fabric script (based on the file 2-do_deploy_web_static.py)
that distributes an archive to your web servers, using the
function deploy:.
fab -f 3-deploy_web_static.py deploy -i ~/.ssh/school -u ubuntu
"""
from fabric.api import *
from os.path import exists, isdir
from datetime import datetime
env.hosts = ['54.146.94.114', '54.172.58.174']


def do_pack():
    """
    A function that generates a .tgx archive from web_static folder
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        filename = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(filename))
        return filename
    except Exception as e:
        return None


def do_deploy(archive_path):
    """
     A function that distributes an archive to the web servers
    """
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except Exception as e:
        return False


def deploy():
    '''
    Deploys my webstatic files to my servers
    '''
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

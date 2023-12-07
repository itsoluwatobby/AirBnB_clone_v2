#!/usr/bin/python3
"""
a Fabric script (based on the file 2-do_deploy_web_static.py)
that distributes an archive to your web servers, using the
function deploy:.
"""
from fabric.api import local, put, env, run
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


env.user = 'ubuntu'
env.hosts = ['54.146.94.114', '54.172.58.174']


def do_deploy(archive_path):
    """
    A function that distributes an archive to the web servers
    """
    if not os.path.isfile(archive_path):
        return False

    # update the /tmp dir
    put(archive_path, '/tmp/')

    # Create dir where file will be extracted to
    filename = archive_path.split('/')[-1]
    dir_path = '/data/web_static/releases/{}'.format(
            filename.split('.')[0])
    run('mkdir -p {}'.format(dir_path))

    # decompress to server folder
    server_archive = '/tmp/' + filename
    run('tar -xzf {} -C {}'.format(server_archive, dir_path))

    # remove archive from web server
    run('rm -rf {}'.format(server_archive))

    # remove symbolic link
    run('rm -rf /data/web_static/current')

    # transfer files from web_static to web_static
    run('mv {}/web_static/* {}'.format(dir_path, dir_path))
    run('rm -rf {}/web_static'.format(dir_path))

    # Create a new symbolic link
    run('ln -s {} /data/web_static/current'.format(dir_path))

    return True


def deploy():
    '''
    Deploys my webstatic files to my servers
    '''
    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)

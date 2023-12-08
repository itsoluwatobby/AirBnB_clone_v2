#!/usr/bin/python3
"""
a Fabric script (based on the file 2-do_deploy_web_static.py)
that distributes an archive to your web servers, using the
function deploy:.
"""
from fabric.api import local, put, env, run
import os
from time import strftime
from datetime import date


def do_pack():
    """
    A function that generates a .tgx archive from web_static folder
    """
    filename = time.strftime("%Y%m%d%H%M%S")

    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(filename))
        return "versions/web_static_{}.tgz".format(filename)
    except Exception as e:
        return None


env.user = 'ubuntu'
env.hosts = ['54.146.94.114', '54.172.58.174']
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """
    A function that distributes an archive to the web servers
    """
    try:
        if not os.path.exists(archive_path):
            return False

        # update the /tmp dir
        put(archive_path, '/tmp/')

        timestamp = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/releases/\
            web_static_{}/'.format(timestamp))

        # decompress archive and delete .tgz
        run('sudo tar -xzf /tmp/web_static_{}.tgz -C /data/web_static\
            /releases/web_static_{}/'.format(timestamp, timestamp))

        run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
            /data/web_static/releases/web_static_{}/'
            .format(timestamp, timestamp))
        # remove extraneous web_static dir
        run('sudo rm -rf /data/web_static/releases/web_static_{}/\
             web_static'.format(timestamp))

        # delete pre-existing sym link
        run('sudo rm -rf /data/web_static/current')

        # re-establish symbolic link
        run('sudo ln -s /data/web_static/releases/web_static_{}/ /data\
            /web_static/current'.format(timestamp))
    except Exception as e:
        return False
    return True


def deploy():
    '''
    Deploys my webstatic files to my servers
    '''
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

#!/usr/bin/python3
"""import fabric, os
"""
from fabric.api import run, put, env
from os.path import exists


env.hosts = ['52.200.50.96', '52.201.160.72']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Distributes an archive to your web servers

    Args:
        archive_path (str): Path to archive to be deployed

    Returns:
        bool: True if all operations are done rght else false
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ dir in web server
        put(archive_path, "/tmp/")

        # Extract the archive to /data/web_static/releases/<
        # archive filename without extension>
        file_name = archive_path.split('/')[-1]
        folder_name = "/data/web_static/releases/{}".format(
                file_name.split('.')[0])
        run('mkdir -p {}'.format(folder_name))
        run('tar -xzf /tmp/{} -C {}'.format(file_name, folder_name))

        # Delete the archive from web server
        run('rm /tmp/{}'.format(file_name))

        # Delete the symbolic link of /data/web_static/current
        # link to new one
        run('rm -f /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(folder_name))

        return True

    except Exception as e:
        print(e)
        return False

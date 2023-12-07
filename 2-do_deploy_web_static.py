#!/usr/bin/python3
"""import fabric, os
"""
from fabric.api import run, put, env
import os


env.hosts = ['52.200.50.96', '52.201.160.72']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Distributes an archive to your web servers

    Args:
        archive_path (str): Path to archive to be deployed

    Returns:
        bool: True if all operations are done rght else false
    """
    if os.path.isfile(archive_path) is False:
        return False

    # Upload the archive to /tmp/ dir on the web server
    # Uncompress the archive to /data/web_static/releases/<filename
    # without extension> on the web server
    filename = archive_path.split("/")[-1]
    name = filename.split(".")[0]

    if put(archive_path, "/tmp/{}".format(filename)).failed is True:
        return False

    release_path = "/data/web_static/releases/{}".format(name)

    if run('rm -rf {}'.format(release_path)).failed is True:
        return False

    if run('mkdir -p {}'.format(release_path)).failed is True:
        return False

    if run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.
            format(filename, name)).failed is True:
        return False

    # Delete the archive
    if run('rm /tmp/{}'.format(filename)).failed is True:
        return False

    # Move content to the correct location
    if run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'.format(name, name)).failed is True:
        return False

    # Remove unnecessary directory
    run('rm -rf {}/web_static'.format(release_path))

    # Create a new symbolic link and delete the old one
    if run('rm -rf /dat/web_static/releases/{}/web_static'.
            format(name)).failed is True:
        return False

    if run('rm -rf /data/web_static/current').failed is True:
        return False

    if run('ln -s /{}/ /data/web_static/current'.
            format(release_path)).failed is True:
        return False

    print("New version deployed!")
    return True

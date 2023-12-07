#!/usr/bin/python3
"""
a Module that contains a do_deploy function.
"""

from fabric.api import env, run, put
from os.path import exists

env.hosts = ['52.200.50.96', '52.201.160.72']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
    A Fabric script that distributes an archive to your web servers
    """

    # Check if the archive file exists
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Extract the archive to /data/web_static/releases/
        # <archive filename without extension>
        filename = archive_path.split('/')[-1]
        folder_name = f"/data/web_static/releases/{filename.split('.')[0]}"
        run(f"mkdir -p {folder_name}")
        run(f"tar -xzf /tmp/{filename} -C {folder_name}")

        # Delete the archive from the web server
        run(f"rm /tmp/{filename}")

        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -f /data/web_static/current")

        # Create a new symbolic link /data/web_static/current
        # linked to the new version
        run(f"ln -s {folder_name} /data/web_static/current")

        return True

    except Exception as e:
        print(e)
        return False

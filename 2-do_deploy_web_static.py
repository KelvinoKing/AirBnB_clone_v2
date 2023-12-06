#!/usr/bin/python3
"""import fabric, os
"""
from fabric.api import run, put, env
import os


env.hosts = ['52.200.50.96', '52.201.160.72']


def do_deploy(archive_path):
    """Distributes an archive to your web servers

    Args:
        archive_path (str): Path to archive to be deployed

    Returns:
        bool: True if all operations are done rght else false
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ dir on the web server
        put(archive_path, "/tmp/")

        # Uncompress the archive to /data/web_static/releases/<filename
        # without extension> on the web server
        archive_filename = os.path.basename(archive_path)
        release_path = "/data/web_static/releases/{}".format(
                archive_filename.split('.')[0])
        run('mkdir -p {}'.format(release_path))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_path))

        # Move contente to the correct location
        run('mv {}/web_static/* {}'.format(release_path, release_path))

        # Remove unnecessary directory
        run('rm -rf {}/web_static'.format(release_path))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(archive_filename))

        # Create a new symbolic link and delete the old one
        current_link = '/data/web_static/current'
        run('rm -rf {}'.format(current_link))
        run('ln -s {} {}'.format(release_path, current_link))

        # Restart Nginx
        run('sudo service nginx restart')

        print("New version deployed!")
        return True

    except Exception as e:
        return False


if __name__ == "__main__":
    import sys
    import argparse

    args = sys.argv[1:]
    for i in range(len(args)):
        if args[i] == '-i' and i + 1 < len(args):
            env.key_filename = args[i + 1]
        elif args[i] == '-u' and i + 1 < len(args):
            env.user = args[i + 1]

    parser = argparser.ArgumentParser()
    parser.add_argument('--archive_path', required=True)
    args = parser.parse_args()

    do_deploy(args.archive_path)

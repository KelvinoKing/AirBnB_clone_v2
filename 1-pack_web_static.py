#!/usr/bin/python3
"""import fabric module
"""
from fabric.api import local
import os
from datetime import datetime


def do_pack():
    """Generate a .tgz archize from the contents of the web_static folder
    of your AirBnB Clone repo

    Returns:
        str: return the archive path if the archive has been
             correctly generated. Otherwise, it should return None
    """
    try:
        # Creates version folder if does not exist
        local('mkdir -p versions')

        # Generate name file
        # web_static_<year><month><day><hour><minute><second>.tgz
        my_time = datetime.utcnow()
        file_name = "web_static_{}{}{}{}{}{}.tgz".format(
                my_time.year, my_time.month, my_time.day, my_time.hour,
                my_time.minute, my_time.second)

        # Create the archive
        local('tar -cvzf versions/{} web_static'.format(file_name))

        # Return the archive path
        return os.path.join("version", file_name)

    except Exception as e:
        return None


if __name__ == "__main__":
    do_pack()

#!/usr/bin/python3
"""import fabric modules
"""
import os
from fabric.api import *


def do_clean(number=0):
    """Deletes out-of-date archives.
    Args:
        number (int): The number of archives to keep,
        including the most recent.Default is 0.
    """

    number = int(number)
    if number < 0:
        return
    if number == 0:
        number = 1

    with lcd("versions"):
        local("ls -1t | tail -n +{} | xargs rm -f".format(number + 1))

    with cd("/data/web_static/releases"):
        run("ls -1t | tail -n +{} | xargs rm -rf".format(number + 1))

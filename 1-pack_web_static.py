#!/usr/bin/python3
"""
Fabric scipt that generates a .tgz archive from the content of the
web_static folder of our AirBnB Clone repo, using the function do_pack.
"""


from fabric.api import local
from time import strftime as stf
import os.path
from os import path


def do_pack():
    """Function that does a pack with the files of the folder web_static."""
    if path.exists('versions/') is False:
        local("mkdir versions/")
    filename = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        stf("%Y"),
        stf("%m"),
        stf("%d"),
        stf("%H"),
        stf("%M"),
        stf("%S"))
    a = local("tar -cvzf {} web_static".format(filename))
    if a.failed is True:
        return None
    return filename

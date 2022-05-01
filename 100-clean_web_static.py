#!/usr/bin/python3
"""
Fabric script (based on the file 3-deploy_web_static.py) that deletes
out-of-date archives, using the function do_clean.
"""

from fabric.api import local
from fabric.api import run
from fabric.api import put
from fabric.api import env
from fabric.api import lcd
from fabric.api import cd
import os.path
from os import path
from time import strftime as stf


env.hosts = ['34.74.115.199', '34.74.58.247']


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


def do_deploy(archive_path):
    """ Function that deploys archive path. """
    if path.exists(archive_path) is False:
        return False

    no_ver = archive_path.split("/")
    no_ext = no_ver[1].split(".")
    p = "/data/web_static/releases"

    a = put("versions/{}".format(no_ver[1]), "/tmp/{}".format(no_ver[1]))
    if a.failed is True:
        return False
    a = run("mkdir -p /data/web_static/releases/{}".format(no_ext[0]))
    if a.failed is True:
        return False
    a = run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
        no_ver[1], no_ext[0]))
    if a.failed is True:
        return False
    a = run("rm /tmp/{}".format(no_ver[1]))
    if a.failed is True:
        return False
    a = run("mv {}/{}/web_static/* {}/{}/"
            .format(p, no_ext[0], p, no_ext[0]))
    if a.failed is True:
        return False
    a = run("rm -rf /data/web_static/releases/{}/web_static"
            .format(no_ext[0]))
    if a.failed is True:
        return False
    a = run("rm -rf /data/web_static/current")
    if a.failed is True:
        return False
    a = run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(no_ext[0]))
    if a.failed is True:
        return False
    print("New version deployed!")
    return True


def deploy():
    """ Function that deploys static content. """
    archive = do_pack()
    if archive is None:
        return False
    return (do_deploy(archive))


def do_clean(number=0):
    """ Function that deletes the archive out of date. """
    with lcd("versions/"):
        a = local("ls -1t", capture=True)
        elmts = a.split("\n")
        if int(number) <= 1:
            to_rm = elmts[1:len(elmts)]
        else:
            to_rm = elmts[int(number):len(elmts)]
        for elmt in to_rm:
            local("rm {}".format(elmt))

    with cd("/data/web_static/releases"):
        a = run("ls -1t")
        elmts = a.split("\n")
        if int(number) <= 1:
            to_remove = elmts[1:len(elmts)]
        else:
            to_remove = elmts[int(number):len(elmts)]
        for elmt in to_remove:
            if elmt == "test":
                continue
            else:
                run("rm -rf {}".format(elmt))

#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py) that creates and
distributes an archive to your web servers, using the function deploy.
"""

import os
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy

archive = do_pack()


def deploy():
    """ Function that deploys static content. """
    if archive is None:
        return False
    return (do_deploy(archive))

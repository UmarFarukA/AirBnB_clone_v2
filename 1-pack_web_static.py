#!/usr/bin/python3
"""Generates a Fabfile to generates a .tgz from the contents of web static"""

import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a .tgz archive for web static content"""
    dt = datetime.utcnow()
    file = f"versions/web_static_{dt.year}{dt.month}{dt.day}\
            {dt.hour}{dt.minute}{dt.second}"
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").Failed is True:
            return None
    if local(f"tar -cvzf {file} web_static").Failed is True:
        return None
    return file

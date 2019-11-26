"""
This module is currently being worked upon. Please contact Harshit Lakhotia or
Lukas Grünhaupt for more info.
"""
from pathlib import Path
import os
import shutil

from qcodes import initialise_or_create_database_at


def initialise_db_at(database_path, mirror_from_level=6):
    """
     This function is used  to initialise your database at the database_path
     Args:
         database_path: Path where you want your db files to be stores
         mirror_from_level: Everything after this level needs to be mirrored
            to the destination directory.
    """
    curr_path = Path.cwd()
    default_path = Path(database_path)
    parts_curr_path = curr_path.parts
    dest_dir = Path(default_path, *parts_curr_path[mirror_from_level:])
    dest_path = Path.joinpath(dest_dir, 'experiments.db ')
    initialise_or_create_database_at(dest_path)


def ig_f(dir, files):
    return [f for f in files if os.path.isfile(os.path.join(dir, f))]


def copytree(src, dst, symlinks=False, ignore=ig_f, print_error=False):
    """
    TODO: Write doctstrings

    Usage
    >>> src = r'C:\Users\a-halakh\Documents\Microsoft\QcodesHarshit'
    >>> dst = r'C:\Users\a-halakh\Music\QcodesData'
    >>> copytree(src, dst)
    """
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            try:
                shutil.copytree(s, d, symlinks, ignore)
            except OSError as e:
                if print_error:
                    print(e)
                copytree(s, d)

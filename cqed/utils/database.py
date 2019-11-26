"""
This module is currently being worked upon. Please contact Harshit Lakhotia or
Lukas Grünhaupt for more info.
"""
from pathlib import Path

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

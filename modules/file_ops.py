import os
from .utils import dirs
import shutil

def create_dir(dir):
    if not os.path.isdir(dir):
        os.makedirs(dir)
        return {"success": True, "data": {"path": dir}}
    return {"success": False}

def list_themes():
    themes = os.listdir(dirs.THEMES_DIR)
    return themes

def copy_folders(src, dst):
    # TODO delete debug symbol
    print("COPY_FOLDER func: ", src, dst)
    try:
        shutil.copytree(src, dst)
        return {"success": True}
    except Exception as e:
        return {"success": False}

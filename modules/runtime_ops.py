from . import file_ops
from . import build_ops
from .utils import dirs

import pathlib

def init_new_project(project_name, project_dir, build_dir, project_theme):
    project_name = project_name
    project_dir = f"{project_dir}/{project_name}"
    build_dir = f"{build_dir}"
    project_theme = project_theme
    themes_list = file_ops.list_themes()

    # print(project_name, project_dir, build_dir, project_theme)
    # print(themes_list)
    # print(project_theme)

    # Theme check and set project theme
    if project_theme in themes_list:
        project_theme_dir = f"{dirs.THEMES_DIR}/{project_theme}"
    else:
        usr_input = input(f"[!] Theme {project_theme} not found in themes directory, using default theme instead? (y/n) ")
        if usr_input == "y":
            project_theme_dir = f"{dirs.THEMES_DIR}/default"
        elif usr_input == "n":
            print("Exiting...")
            exit()
        else:
            print("Unknown option, exiting...")
            exit()
    
    # Check & create project dir
    print("[+] Creating project directory")
    response = file_ops.create_dir(project_dir)
    if not response['success']:
        print("[!] Failed on creating project directory, make sure you have permission to write in this directory, exiting...")
        exit()

    print("[+] Creating build directory")
    reponse = file_ops.create_dir(build_dir)
    if not response['success']:
        print("[!] Failed on creating build directory, make sure you have permission to write in this directory, exiting...")
        exit()

    print("[+] Applying theme")
    response = file_ops.copy_folders(project_theme_dir, f"{dirs.BUILD_DIR}/{project_name}")
    if not reponse["success"]:
        print("[!] Failed on copying theme, make sure you have permission to write in this directory, exiting...")
        exit()
    
    print("[+] Building default pages")
    # TODO finish build init new project pages
    build_ops.init_new_project_pages(project_name, project_dir, build_dir, project_theme)

    print(f"[+] Success on creating new project {project_name}")
    print(f"""
    Note:
    available page are: home, about, contact
    posts will be added to the folder "posts" inside project directory
    to edit a page use "--edit", Ex: fullmetal --project <project_name> --edit <page_file_name>.html
    to add new posts use "--npost", Ex: fullmetal --project <project_name> --npost
    for a full commands list, please see documentations.
    """)


# TODO create new page

# TODO create new post

# TODO build project

# TODO run local server for preview
import argparse
import os
from modules.utils import dirs
from modules import runtime_ops

parser = argparse.ArgumentParser()

print("""
 ▄▖  ▜ ▜   ▖  ▖  ▗   ▜ 
 ▙▖▌▌▐ ▐ ▄▖▛▖▞▌█▌▜▘▀▌▐ 
 ▌ ▙▌▐▖▐▖  ▌▝ ▌▙▖▐▖█▌▐▖

 Static Site Generator
 By https://zagdiablo.github.io/
""")

parser.add_argument("--init", action="store_true", help="Initiate a new project")
parser.add_argument("--name", type=str, help="Project name")
parser.add_argument("--dir", type=str, help="Project to save directory")
parser.add_argument("--out", type=str, help="Build output directory")
parser.add_argument("--theme", type=str, help="Specify a theme")
args = parser.parse_args()

project_name = "website_1"
project_dir = f"{dirs.PROJECT_DIR}"
build_dir = f"{dirs.BUILD_DIR}"
project_theme = "default"

if args.init:
    if args.name:
        project_name = args.name
    if args.dir:
        project_dir = f"{args.dir}"
    if args.out:
        build_dir = f"{args.out}"
    if args.theme:
        project_theme = args.theme
    runtime_ops.init_new_project(project_name, project_dir, build_dir, project_theme)
else:
    parser.print_help()
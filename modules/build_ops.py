import pathlib
from .utils import dirs
from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader
from json import load

template_env = Environment(loader=FileSystemLoader(searchpath="/"))

def init_new_project_pages(project_name, project_dir, build_dir, project_theme):
    # generate index.md for the home page
    with open(f"{project_dir}/index.md", "w") as f:
        f.writelines("#this is title\n\nthis is the content")

    template = template_env.get_template(f"{dirs.THEMES_DIR}/{project_theme}/index.html")

    with open(f"{project_dir}/index.md") as f:
        article = markdown(f.read())

    with open(f"{build_dir}/{project_name}/index.html", "w") as f:
        f.write(
            template.render(
                title = "test page",
                article=article
            )
        )
    # TODO do other pages generation
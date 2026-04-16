from pathlib import Path

help = """
Your project has been created!

Initialize your new project with:

cd {{cookiecutter.repo_name}}
uv sync

Enjoy!
"""
print(f"{Path.cwd()=}")
print(help)

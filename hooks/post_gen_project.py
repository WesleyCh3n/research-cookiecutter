import subprocess

subprocess.run(["git", "init"], check=True)

help = """
Your project has been created!

Initialize your new project with:

cd {{cookiecutter.repo_name}}
uv sync

Enjoy!
"""

print(help)

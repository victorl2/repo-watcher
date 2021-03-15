# My Repo watcher

This project uses [gitpython](https://gitpython.readthedocs.io/en/stable/intro.html) to watch for changes in a repository, it will execute the `run.sh` script after a it identifies changes in the repository on the local git repository, it will pull the changes and after it try to run the script.

# Install and usage
+ You must have a recent version of [python](https://www.python.org/) installed.
+ Clone the repository you want watch in your local environment.
+ Inside the project folder run `pip install -r requirements.txt`
+ Also inside the project folder run `python main.py ./my-repository` to start the project

Done !! you will be watching for changes in the target repo

# My Repo watcher

This project uses [gitpython](https://gitpython.readthedocs.io/en/stable/intro.html) to watch for changes in a repository, it will execute the `run.sh` script after a it identifies changes in the repository on the local git repository, it will pull the changes and after it try to run the script.

# Install and usage
+ Having a local repository inside the project folder
+ Inside the project folder run `pip install -r requirements.txt`
+ Also inside the project folder run `python3 main.py ./my-repository` to start the project

Done !! you will be watching for changes in the target repo
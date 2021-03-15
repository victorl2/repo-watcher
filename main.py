from git import Repo
import subprocess
import time
import sys

def git_pull_change(path):
    repo = Repo(path)
    current = repo.head.commit

    repo.remotes.origin.pull()

    if current == repo.head.commit:
        print("Repo not changed. Sleep mode activated.")
        return False
    else:
        print("Repo changed! Activated.")
        return True

if __name__ == '__main__':
    if len(sys.argv) == 0:
        print("you must provide the relative path for the local repository you want to watch. ex: ./my-repository")

    while True:
        if git_pull_change(sys.argv[1]):
            time.sleep(1)
            subprocess.call(['sh', './run.sh'])
        time.sleep(60)

            
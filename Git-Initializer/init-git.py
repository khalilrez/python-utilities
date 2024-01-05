import subprocess
import argparse

def createLocalRepo():
    subprocess.run(["git init -b main"],shell=True,executable="/bin/bash")
    subprocess.run(["git add ."],shell=True,executable="/bin/bash")
    subprocess.run(["git commit -m 'Initial Commit'"],shell=True,executable="/bin/bash")

def createRemoteRepo():
    username = input("Enter your github username: ")
    repo_name = input("Enter the name of the repository: ")
    print("Creating remote repository...")
    print("Please enter your github token when prompted")
    subprocess.run(['curl', '-u', username, 'https://api.github.com/user/repos', '-d', f'{"name":"{repo_name}"}'],shell=True,executable="/bin/bash")
    subprocess.run([f"git remote add origin https://github.com/{username}/{repo_name}.git"],shell=True,executable="/bin/bash")

def pushToRemote():
    subprocess.run(["git push"],shell=True,executable="/bin/bash")

def addAndCommit():
    commit_message = input("Enter commit message: ")
    subprocess.run(["git add ."],shell=True,executable="/bin/bash")
    subprocess.run([f"git commit -m '{commit_message}'"],shell=True,executable="/bin/bash")




def mainMenu(args):
    exitSignal = 0
    while exitSignal!=1:
        print("Welcome to Git-Initializer")
        print("1. Create a local repository")
        print("2. Create a remote repository")
        print("3. Push to remote repository")
        print("4. Add and commit")
        print("0. Exit")
        if args.create:
            createLocalRepo()
        elif args.remote:
            createRemoteRepo()
        elif args.push:
            pushToRemote()
        elif args.add:
            addAndCommit()
        else:
            choice = input("Enter your choice: ")
        if choice == "1":
            createLocalRepo()
        elif choice == "2":
            createRemoteRepo()
        elif choice == "3":
            pushToRemote()
        elif choice == "4":
            addAndCommit()
        elif choice == "0":
            exitSignal = 1
        else:
            print("Invalid choice")
        


parser = argparse.ArgumentParser(description='Git-Initializer, a simple python script to initialize a git repository\n. Use without any arguments to run the script in interactive mode')
parser.add_argument('-c', '--create', action='store_true', help='Create a local repository')
parser.add_argument('-r', '--remote', action='store_true', help='Create a remote repository')
parser.add_argument('-p', '--push', action='store_true', help='Push to remote repository')
parser.add_argument('-a', '--add', action='store_true', help='Add and commit')
args = parser.parse_args()
mainMenu(args)
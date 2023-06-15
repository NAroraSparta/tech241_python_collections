```gitexclude
What is Git?

Git is a distributed version control system that allows developers 
to track changes in their codebase, collaborate with others, and manage 
different versions of their projects. It was created by Linus Torvalds, 
the same person who developed the Linux operating system.
With Git, developers can create a repository to store their project's files 
and track changes made to those files over time. Each time a developer 
makes a change to a file, Git records it as a separate commit. 
Commits represent a specific version of the project, and developers 
can easily switch between different commits to review changes or 
revert back to a previous state.
```
```gitexclude
Git is designed to work efficiently with both small and large projects, 
handling changes across multiple branches and allowing developers 
to merge those changes together. It also enables collaboration among 
developers by providing features like branch management, conflict resolution, 
and remote repository hosting platforms like GitHub, GitLab, and Bitbucket.
```
```gitexclude
One of the key ADVANTAGES of Git is its distributed nature. 
It is called Distributed Version Control System.
Each developer working on a project has a complete copy of the repository, 
including the entire history of commits. This means that developers 
can work offline and independently, making local commits, 
and later synchronize their changes with the remote repository when they are ready.
```
```gitexclude
Some main git commands:
git --version   To check the version of git installed on your system
git config --global user.name "<user_name>"     To give a user name to your git hub account
git config --global user.email "<email_id>"    To configure your email id for the account
git init        To change directory into local repository
git status      To check the status of the named repository  
git add <file_name> To add a particular file to Staging area
git add .   To add all files from working directory to Staging area
.
```
```gitexclude
git log    To see the repo's commit history. The output includes the commit ID, commit author, 
           developer email, commit date and commit message string for each 
           commit on the active branch.
```
```gitexclude
git commit -m "<Commit_message>"    To create a new commit in Git with a specified commit message

A commit in Git represents a snapshot of the project at a particular point in time. 
It includes all the changes made to the files since the last commit. 
Each commit has a unique identifier called a commit hash, 
which allows you to refer to it later.
```
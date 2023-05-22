# Git Workflow

## When you start to do something new

Create a new branch for every new feature. Publish the branch and open a pull request early on - this helps to avoid merge conflicts.

```bash
# Pull the changes
$ git pull 

# Checkout to another branch (i.e. jonijoensuu/frontend-skeleton)
$ git checkout -b <your-name/branch-name>

# Commit your changes
$ git add -A $ git commit -m <your-comment>

# Make sure you do not miss changes other have done
$ git pull

# Push the code to Github
$ git push origin <name-of-your-branch>
```

Add text "Closes" and the issue number at the beginning of your pull request comment. 

`Closes #<issue-number>`

When a pull request is merged, the issue is then automatically closed. Create a task in the sprint backlog, if you are missing a suitable issue.

## When you review pull requests

Always test the changes locally in our own environment before giving a review. 
```bash
$ git fetch origin

# Checkout to the reviewed branch
$ git checkout <branch-name>

# Pull the changes in the branch
$ git pull origin <branch-name>
```

Make sure you understand what the code does. 

If you do some minor fixes, you can make a commit to the same branch. If there is a need to make more changes, add your review comments and choose then *Request changes*.





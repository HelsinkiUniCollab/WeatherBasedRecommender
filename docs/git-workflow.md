# Git Workflow and branching

## Create a new branch for every new feature. 

`$ git pull` 

`$ git checkout -b <your-name/branch-name>` (i.e. jonijoensuu/frontend-skeleton)

`$ git add -A $ git commit -m "<your-comment>"` 

`$ git pull`   (to make sure you do not miss changes other have done)

`$ git push origin <name-of-your-branch>`

Publish a branch and open pull request early on - this helps to avoid merge conflicts.

Add text "Closes" and the issue number at the beginning of your pull request comment. When a pull request is merged, issue is automatically closed. If there is no issue ready, create a task in the sprint backlog.

`Closes #<issue-number>`

## Reviewing a pullrequest by another team member

Always test the changes locally in our own environment before giving a review.

Workflow for fetch the branch.

`$ git fetch origin` 

`$ git checkout <branch-name>` 

`$ git pull origin <branch-name>`

If you do some minor fixes, you can make a commit to the same branch.
If there is a need to make more changes, add comments and choose Request changes in review.





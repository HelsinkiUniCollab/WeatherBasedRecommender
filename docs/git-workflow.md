# Git WorkFlow and branching

Create a new branch for every new feature. 

`$ git pull` 
`$ git checkout -b <some-descriptive-branch-name>` 
`$ git add -A $ git commit -m "<your-comment>"` 
`$ git pull`   (to make sure you do not miss changes other have done)
`$ git push origin <name-of-your-branch>`


Workflow when you are reviewing a pullrequest by another team member.
`$ git fetch origin` 
`$ git checkout <branch-name>` 
`$ git pull origin <branch-name>`

If you do some minor fixes, you can make a commit to the same branch.



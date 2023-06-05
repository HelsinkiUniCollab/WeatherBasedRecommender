from invoke import task

@task
def start(ctx):
    ctx.run("poetry run flask --app src/app --debug run", pty=True)

@task
def test(ctx):
    ctx.run("poetry run pytest src/tests", pty=True)

@task
def pylint(ctx):
    ctx.run("poetry run pylint src", pty=True)
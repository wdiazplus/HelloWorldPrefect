from prefect import task,Flow

@task
def hello():
    print("Hello world from Prefect")

with Flow("hello_flow") as Hello:
    hello()

Hello.run()
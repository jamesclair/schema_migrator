import typer

app = typer.Typer()


@app.command()
def showmigrations(): ...


@app.command()
def migrate(name: str): ...


if __name__ == "__main__":
    app()

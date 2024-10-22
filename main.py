import typer
from expense import add_expense

app = typer.Typer()

@app.command()
def add(description: str = "", amount: int = 0):
    if not description or amount == 0:
        raise ValueError("[bold red]Error:[/bold red] Please provide a description and amount.")
    
    add_expense(description, amount)
    
if __name__ == "__main__":
    app() 
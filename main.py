import typer
from rich import print

app = typer.Typer()

@app.command()
def add(description: str = "", amount: int = 0):
    if not description or amount == 0:
        print(f"[bold red]Error:[/bold red] Please provide a description and amount.")
        return
    
    print(description, amount)
    
if __name__ == "__main__":
    app() 
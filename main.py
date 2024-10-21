import typer
from rich import print
from csv import writer

app = typer.Typer()

@app.command()
def add(description: str = "", amount: int = 0):
    if not description or amount == 0:
        raise ValueError("[bold red]Error:[/bold red] Please provide a description and amount.")
    
    with open("tracker.csv", "a") as f:
        writer_obj = writer(f)
        writer_obj.writerow([description, amount])
        
        f.close()
    
if __name__ == "__main__":
    app() 
import typer
import csv
from rich import print

from expense import add_expense, get_total_expense
from utils import show_table

app = typer.Typer()

@app.command()
def list():
    with open("tracker.csv", "r") as f:
        csv_reader = csv.reader(f)

        #Skip header
        next(csv_reader, None)
        
        show_table(csv_reader)
        
@app.command()
def summary():
    total = get_total_expense()
    print(f"Total expenses: ${total}")

@app.command()
def add(description: str = "", amount: int = 0):
    if not description or amount == 0:
        raise ValueError("[bold red]Error:[/bold red] Please provide a description and amount.")
    
    add_expense(description, amount)
    
if __name__ == "__main__":
    app() 
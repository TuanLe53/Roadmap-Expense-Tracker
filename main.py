import typer
import csv
from rich import print

from expense import add_expense, get_total_expense, delete_expense_record
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
    
@app.command()
def delete(id: str = ""):
    if not id:
        raise ValueError("[bold red]Error:[/bold red] Please provide an expense record's id.")
    
    delete_expense_record(id)
    print("Done")
    
if __name__ == "__main__":
    app() 
import typer
import csv
from rich import print

from expense import add_expense, get_total_expense, delete_expense_record, get_expense_of_month, get_expense, update_expense_record
from utils import show_table

app = typer.Typer()

@app.command()
def list(month: int = 0):
    if 1 <= month <= 12:
        data = get_expense_of_month(month)
        show_table(data)
    elif month == 0:        
        with open("tracker.csv", "r") as f:
            csv_reader = csv.reader(f)

            #Skip header
            next(csv_reader, None)
            
            show_table(csv_reader)
    else:
        raise ValueError("[bold red]Error:[/bold red] Invalid input! The program only accepts month values from 1 to 12, or you can leave it blank to get a report for all 12 months.")
    
        
@app.command()
def summary(month: int = 0):
    if 1 <= month <= 12:
        expenses = get_expense_of_month(month)
        total = get_total_expense(expenses)
        print(f"Total expenses: ${total}")
    elif month == 0:
        with open("tracker.csv", "r") as f:
            expenses = csv.reader(f)
            #Skip header
            next(expenses, None)
            total = get_total_expense(expenses)
        print(f"Total expenses: ${total}")
    else:
        raise ValueError("[bold red]Error:[/bold red] Invalid input! The program only accepts month values from 1 to 12, or you can leave it blank to get a report for all 12 months.")
 
@app.command()
def add(description: str = "", amount: int = 0):
    if not description or amount == 0:
        raise ValueError("[bold red]Error:[/bold red] Please provide a description and amount.")
    
    add_expense(description, amount)
    print(f"[bold green]Success:[/bold green] Added expense '{description}' with amount {amount:,}.")
    
@app.command()
def update(id: str= "", description: str = None, amount: int = None):
    if not id:
        print("[bold red]Error:[/bold red] ID is required.")
        return
    
    expense = get_expense(id)
    if not expense:
        print("[bold red]Error:[/bold red] Not found")
        return
    
    if not description and amount is None:
        raise ValueError("[bold red]Error:[/bold red] Please provide a description and amount.")

    if description:
        expense[1] = description
    if amount is not None and amount > 0:
        expense[2] = amount
    update_expense_record(id, expense)
    
@app.command()
def delete(id: str = ""):
    if not id:
        raise ValueError("[bold red]Error:[/bold red] Please provide an expense record's id.")
    expense = get_expense(id)
    if not expense:
        print("[bold red]Error:[/bold red] Not found")
        return
    
    delete_expense_record(id)
    print("Done")
    
if __name__ == "__main__":
    app() 
from rich.table import Table
from rich.console import Console

def show_table(data):
    table = Table(show_header=True)
    table.add_column("Description")
    table.add_column("Price")
    
    for row in data:
        table.add_row(row[0], row[1])
        
    console = Console()
    console.print(table)
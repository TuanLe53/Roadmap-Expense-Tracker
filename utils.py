from rich.table import Table
from rich.console import Console
from csv import writer

def show_table(data):
    table = Table(show_header=True)
    table.add_column("ID")
    table.add_column("Description")
    table.add_column("Price")
    table.add_column("Date")
    
    for row in data:
        table.add_row(row[0], row[1], row[2], row[3])
        
    console = Console()
    console.print(table)
    
def write_csv_file(file_name: str, columns: list[str], data: list[list[str]]):
    with open(file_name, "w") as f:
        writer_obj = writer(f, lineterminator="\n")
        writer_obj.writerow(columns)
        
        for record in data:
            writer_obj.writerow(record)
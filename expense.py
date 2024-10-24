import uuid
from csv import writer, reader
from datetime import datetime

def add_expense(description: str, amount: int) -> None:
    id = uuid.uuid4()
    current_date = datetime.today().strftime("%Y-%m-%d")
    with open("tracker.csv", "a") as f:
        writer_obj = writer(f, lineterminator="\n")
        writer_obj.writerow([id, description, amount, current_date])
        
        f.close()
        
def get_expense_of_month(month: int):
    with open("tracker.csv", "r") as f:
        csv_reader = reader(f)

        #Skip header
        next(csv_reader, None)
        
        results = [expense for expense in csv_reader if datetime.strptime(expense[3], "%Y-%m-%d").month == month ]

    return results

def get_total_expense(expenses) -> int:
    total = 0
    for row in expenses:
        total += int(row[2])
    
    return total
    
def delete_expense_record(id: str) -> None:
    with open("tracker.csv", "r") as f:
        csv_reader = reader(f)
        
        #Skip header
        next(csv_reader, None)
        
        new_records = [record for record in csv_reader if record[0] != id]
    
    with open("tracker.csv", "w") as f:
        writer_obj = writer(f, lineterminator="\n")
        writer_obj.writerow(["id", "description", "price", "date"])
        
        for record in new_records:
            writer_obj.writerow(record)
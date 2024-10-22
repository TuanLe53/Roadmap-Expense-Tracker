from csv import writer

def add_expense(description: str, amount: int) -> None:
    with open("tracker.csv", "a") as f:
        writer_obj = writer(f, lineterminator="\n")
        writer_obj.writerow([description, amount])
        
        f.close()
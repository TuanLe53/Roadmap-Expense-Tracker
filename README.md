# Roadmap-Expense-Tracker


## Usage
- Show help
```sh
python .\main.py --help
```

- `list`: List expenses
```sh
python .\main.py list #List all expenses
python .\main.py list --month 11 #List expenses of specific month
```


- `add`: Add a new expense
```sh
python .\main.py add --description "Milk" --amount 10
```


- `summary`: Get a summary of all expenses
```sh
python .\main.py summary #Get a summary of all expenses
python .\main.py summary --month 11 #Get a summary of all expenses for a specific month
```


- `delete`:  Delete an expense by id
```sh
python .\main.py delete --id "expense_id"
```
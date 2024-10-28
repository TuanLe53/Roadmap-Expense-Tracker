# Roadmap-Expense-Tracker

## Description
The Expense Tracker CLI is a command-line tool  designed to help users track and manage their personal finances directly from the terminal. This CLI enables users to add, view, update, and delete expenses with ease.

It is inspired by the [Expense Tracker](https://roadmap.sh/projects/expense-tracker) project from [roadmap.sh](https://roadmap.sh/).

## Installation
1. **Clone the Repository**:
   ``` python
   git clone https://github.com/TuanLe53/Roadmap-Expense-Tracker.git
   cd expense-tracker-cli
2. Create and Activate a Virtual Environment
   ```sh
   python -m venv env

   # On Windows:
   .\env\Scripts\activate

   # On macOS and Linux:
   source env/bin/activate
   ```
3. Install Dependencies
   ```sh
   pip install -r requirements.txt
   ```

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

- `update`: Update an expense by id
```sh
python .\main.py update --id "expense_id" --description "New description" --amount 30
python .\main.py update --id "expense_id" --description "New description" #Update only description
python .\main.py update --id "expense_id" --amount 30 #Update only amount
```
from fastapi import FastAPI, HTTPException
import json
import os

app = FastAPI()

EXPENSES_FILE = 'expenses.json'

if not os.path.exists(EXPENSES_FILE):
    with open(EXPENSES_FILE, 'w') as f:
        json.dump([], f)

def get_expenses():
    with open(EXPENSES_FILE, 'r') as f:
        return json.load(f)

def save_expenses(expenses):
    with open(EXPENSES_FILE, 'w') as f:
        json.dump(expenses, f)

@app.get('/api/expenses')
def get_all_expenses():
    return get_expenses()

@app.post('/api/expenses')
def add_expense(expense: dict):
    expenses = get_expenses()
    expense['id'] = len(expenses) + 1
    expenses.append(expense)
    save_expenses(expenses)
    return expense

@app.delete('/api/expenses/{id}')
def delete_expense(id: int):
    expenses = get_expenses()
    new_expenses = [e for e in expenses if e['id'] != id]
    save_expenses(new_expenses)
    return {'message': 'Expense deleted'}

@app.get('/api/expenses/summary')
def get_summary():
    expenses = get_expenses()
    summary = {}
    for e in expenses:
        summary[e['category']] = summary.get(e['category'], 0) + e['amount']
    return summary

# Serve static files (frontend)
app.mount('/static', StaticFiles(directory='static'), name='static')

# Index route for frontend
@app.get('/')
def read_root():
    return {'message': 'Expense Tracker API'}
# Expense Tracker

Expense tracker with category breakdown

## Run

```bash
docker compose up -d
# Open http://127.0.0.1:PORT
```

## API

  - GET /api/expense_tracker — list all items
  - POST /api/expense_tracker — add item (send JSON body)
  - PUT /api/expense_tracker/{id} — update item (send JSON body)
  - DELETE /api/expense_tracker/{id} — delete item
  - GET /api/expense_tracker/search?q=term — search items

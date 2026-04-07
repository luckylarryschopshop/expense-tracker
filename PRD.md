# Product Requirements Document: Expense Tracker

## Overview
A web application for tracking expenses with a FastAPI backend and HTML frontend. Users can add expenses, view category summaries, and access a monthly overview.

## Features
- **Add Expense**
  - Fields: amount (numeric), category (dropdown), description (text), date (calendar)
  - Categories: food, transport, entertainment, bills, other

- **Category Summary**
  - Totals per category
  - Visual representation (e.g., bars or pie chart)

- **Monthly View**
  - Filter expenses by month
  - Aggregated spending overview

## Technical Requirements
- Backend: FastAPI (Python)
- Frontend: HTML/CSS/JavaScript
- Data storage: Local database (e.g., SQLite)
- Deployment: Dockerized via `docker compose`

## Acceptance Criteria
- All features must work via browser interface
- Responsive design for desktop/mobile
- Error handling for invalid inputs
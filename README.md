# Commercial Loan Risk Assessment Tool
Dylan Todd
Created: 12.01.23
Updated: 12.04.23

## Project Overview
This Flask-based web application is designed to assess the credit risk of commercial loans. It allows users to input key financial metrics and calculates a risk score based on these inputs.

## Directory Structure
Commercial_Loan_Risk_Assessment/
├── app.py                   # Main Flask application file
├── templates/               # HTML templates for the web interface
│   ├── index.html           # Input form for financial data
│   └── result.html          # Displays the calculated risk score and report
└── README.md                # Project description and instructions

## Setup and Running
- Install Flask: `pip install Flask`
- Clone the repository and navigate to the project directory.
- Run the application: `FLASK_APP=app.py flask run`
- Access the web interface at `http://localhost:5000`.

## Application Flow
- The user inputs financial data on the homepage.
- Upon submission, the app calculates a risk score using financial analysis logic.
- The score and a brief report are displayed on the results page.

## Risk Score Calculation
The risk score is calculated using a formula that considers the following inputs:
- Total Assets
- Total Liabilities
- Net Income
- Operating Cash Flow
- Loan Amount Requested

The calculation reflects basic principles of credit risk assessment in commercial banking.
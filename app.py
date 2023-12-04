# app.py
# Dylan Todd
# Created: 12.01.23
# Updated: 12.04.23

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Extract financial data from form
        total_assets = float(request.form.get('total_assets', 0))
        total_liabilities = float(request.form.get('total_liabilities', 0))
        net_income = float(request.form.get('net_income', 0))
        operating_cash_flow = float(request.form.get('operating_cash_flow', 0))
        loan_amount = float(request.form.get('loan_amount', 0))

        # Calculate risk score
        risk_score = calculate_risk_score(total_assets, total_liabilities, net_income, operating_cash_flow, loan_amount)

        # Generate a basic assessment report
        assessment_report = f"Calculated Risk Score: {risk_score:.2f}"
        return render_template('result.html', assessment_report=assessment_report)
    return render_template('index.html')

def calculate_risk_score(total_assets, total_liabilities, net_income, operating_cash_flow, loan_amount):
    # Example risk calculation logic
    if total_assets == 0:
        return 0
    debt_to_income_ratio = (total_liabilities / total_assets)
    income_ratio = (net_income / total_assets)
    cash_flow_ratio = (operating_cash_flow / loan_amount) if loan_amount != 0 else 0
    score = (income_ratio - debt_to_income_ratio + cash_flow_ratio) * 100
    return max(min(score, 100), 0)  # Ensure score is between 0 and 100

if __name__ == '__main__':
    app.run(debug=True)

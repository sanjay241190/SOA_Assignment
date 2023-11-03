from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for customers
customers = [
    {"customer_id": 1, "name": "Vishal Singh"},
    {"customer_id": 2, "name": "Riya Pandey"},
]

# Sample data for loans
loans = [
    {"loan_id": 1, "customer_id": 1, "amount": 1000, "interest_rate": 5},
    {"loan_id": 2, "customer_id": 2, "amount": 800, "interest_rate": 4.5},
]
################################## C U S T O M E R - L O A N S ########################################


# Get all loans
@app.route('/loans', methods=['GET'])
def get_all_loans():
    return jsonify(loans)

# Get a specific loan by ID
@app.route('/loans/<int:loan_id>', methods=['GET'])
def get_loan(loan_id):
    for loan in loans:
        if loan['loan_id'] == loan_id:
            return jsonify(loan)
    return "Loan not found", 404

# Apply for a new loan
@app.route('/loans', methods=['POST'])
def apply_for_loan():
    data = request.get_json()
    customer_id = data.get("customer_id")
    amount = data.get("amount")
    interest_rate = data.get("interest_rate")
    
    # Check if the customer exists
    customer_exists = any(customer['customer_id'] == customer_id for customer in customers)
    
    if customer_exists:
        new_loan = {
            "loan_id": len(loans) + 1,
            "customer_id": customer_id,
            "amount": amount,
            "interest_rate": interest_rate,
        }
        loans.append(new_loan)
        return jsonify(new_loan), 201
    else:
        return "Customer not found", 400

if __name__ == '__main__':
    app.run(debug=True , port=5004)

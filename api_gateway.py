from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Define the base URLs for each service
ACCOUNTS_BASE_URL = "http://localhost:5001"
CUSTOMERS_BASE_URL = "http://localhost:5002"
TRANSACTIONS_BASE_URL = "http://localhost:5003"
LOANS_BASE_URL = "http://localhost:5004"

# Secret API key for authentication
SECRET_API_KEY = "AAXO90RTT345WWDT"  
# Define routes to proxy requests for account related services

#Authentication @API Gateway

def authenticate_request():
    api_key = request.headers.get("X-API-Key")
    if api_key != SECRET_API_KEY:
        return False
    return True


@app.route('/accounts/<int:account_id>', methods=['GET'])
def get_account_by_id(account_id):
    if not authenticate_request():
        return "Authentication failed", 401
    response = requests.get(f"{ACCOUNTS_BASE_URL}/accounts/{account_id}")
    return (response.text, response.status_code, response.headers.items())

@app.route('/accounts', methods=['POST'])
def create_new_account():
    if not authenticate_request():
        return "Authentication failed", 401
    data = request.get_json()
    response = requests.post(f"{ACCOUNTS_BASE_URL}/accounts", json=data)
    return (response.text, response.status_code, response.headers.items())

@app.route('/accounts/<int:account_id>/deposit', methods=['POST'])
def deposit_in_account(account_id):
    if not authenticate_request():
        return "Authentication failed", 401
    data = request.get_json()
    response = requests.post(f"{ACCOUNTS_BASE_URL}/accounts/{account_id}/deposit", json=data)
    return response.text, response.status_code, response.headers.items()

@app.route('/accounts/<int:account_id>/withdraw', methods=['POST'])
def withdraw_from_account(account_id):
    if not authenticate_request():
        return "Authentication failed", 401
    data = request.get_json()
    response = requests.post(f"{ACCOUNTS_BASE_URL}/accounts/{account_id}/withdraw", json=data)
    return response.text, response.status_code, response.headers.items()

# Define routes to proxy requests for customer related services

@app.route('/customers', methods=['GET'])
def get_all_customers():
    if not authenticate_request():
        return "Authentication failed", 401
    response = requests.get(f"{CUSTOMERS_BASE_URL}/customers")
    return response.text, response.status_code, response.headers.items()

@app.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    if not authenticate_request():
        return "Authentication failed", 401
    data = request.get_json()
    response = requests.put(f"{CUSTOMERS_BASE_URL}/customers/{customer_id}", json=data)
    return response.text, response.status_code, response.headers.items()

@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    if not authenticate_request():
        return "Authentication failed", 401
    response = requests.delete(f"{CUSTOMERS_BASE_URL}/customers/{customer_id}")
    return response.text, response.status_code, response.headers.items()

@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    if not authenticate_request():
        return "Authentication failed", 401
    response = requests.get(f"{CUSTOMERS_BASE_URL}/customers/{customer_id}")
    return response.text, response.status_code, response.headers.items()

@app.route('/customers', methods=['POST'])
def create_customer():
    if not authenticate_request():
        return "Authentication failed", 401
    data = request.get_json()
    response = requests.post(f"{CUSTOMERS_BASE_URL}/customers", json=data)
    return response.text, response.status_code, response.headers.items()


# Define routes for transaction-related operations

@app.route('/transactions', methods=['GET'])
def get_all_transactions():
    if not authenticate_request():
        return "Authentication failed", 401
    response = requests.get(f"{TRANSACTIONS_BASE_URL}/transactions")
    return response.text, response.status_code, response.headers.items()

@app.route('/transactions/<int:transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    if not authenticate_request():
        return "Authentication failed", 401
    response = requests.get(f"{TRANSACTIONS_BASE_URL}/transactions/{transaction_id}")
    return response.text, response.status_code, response.headers.items()

@app.route('/transactions', methods=['POST'])
def create_transaction():
    if not authenticate_request():
        return "Authentication failed", 401
    data = request.get_json()
    response = requests.post(f"{TRANSACTIONS_BASE_URL}/transactions", json=data)
    return response.text, response.status_code, response.headers.items()


# Define routes for loan-related operations

@app.route('/loans', methods=['GET'])
def get_all_loans():
    if not authenticate_request():
        return "Authentication failed", 401
    response = requests.get(f"{LOANS_BASE_URL}/loans")
    return response.text, response.status_code, response.headers.items()

@app.route('/loans/<int:loan_id>', methods=['GET'])
def get_loan(loan_id):
    if not authenticate_request():
        return "Authentication failed", 401
    response = requests.get(f"{LOANS_BASE_URL}/loans/{loan_id}")
    return response.text, response.status_code, response.headers.items()

@app.route('/loans', methods=['POST'])
def apply_for_loan():
    if not authenticate_request():
        return "Authentication failed", 401
    data = request.get_json()
    response = requests.post(f"{LOANS_BASE_URL}/loans", json=data)
    return response.text, response.status_code, response.headers.items()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

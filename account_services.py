from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for bank accounts
accounts = [
    {"account_id": 1, "balance": 1000},
    {"account_id": 2, "balance": 500},
]

############################################### A C C O U N T ############################################

# Get account details by ID
@app.route('/accounts/<int:account_id>', methods=['GET'])
def get_account(account_id):
    for account in accounts:
        if account['account_id'] == account_id:
            return jsonify(account)
    return "Account not found", 404

# Create a new account
@app.route('/accounts', methods=['POST'])
def create_account():
    data = request.get_json()
    new_account = {
        "account_id": len(accounts) + 1,
        "balance": data.get("initial_balance", 0)
    }
    accounts.append(new_account)
    return jsonify(new_account), 201

# Deposit money into an account
@app.route('/accounts/<int:account_id>/deposit', methods=['POST'])
def deposit(account_id):
    data = request.get_json()
    amount = data.get("amount")
    for account in accounts:
        if account['account_id'] == account_id:
            account['balance'] += amount
            return jsonify(account)
    return "Account not found", 404

# Withdraw money from an account
@app.route('/accounts/<int:account_id>/withdraw', methods=['POST'])
def withdraw(account_id):
    data = request.get_json()
    amount = data.get("amount")
    for account in accounts:
        if account['account_id'] == account_id:
            if account['balance'] >= amount:
                account['balance'] -= amount
                return jsonify(account)
            else:
                return "Insufficient balance", 400
    return "Account not found", 404
    
if __name__ == '__main__':
    app.run(debug=True , port=5001)
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for bank accounts
accounts = [
    {"account_id": 1, "balance": 1000},
    {"account_id": 2, "balance": 500},
]
# Sample data for transactions 
transactions = [
    {"transaction_id": 1, "from_account": 1, "to_account": 2, "amount": 100},
    {"transaction_id": 2, "from_account": 2, "to_account": 1, "amount": 50},
]


########################################## T R A N S A C T I O N S #########################################

# Get all transactions
@app.route('/transactions', methods=['GET'])
def get_all_transactions():
    return jsonify(transactions)

# Get a specific transaction by ID
@app.route('/transactions/<int:transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    for transaction in transactions:
        if transaction['transaction_id'] == transaction_id:
            return jsonify(transaction)
    return "Transaction not found", 404

# Create a new transaction
@app.route('/transactions', methods=['POST'])
def create_transaction():
    data = request.get_json()
    from_account = data.get("from_account")
    to_account = data.get("to_account")
    amount = data.get("amount")
    
    # Check if both accounts exist
    from_account_exists = any(account['account_id'] == from_account for account in accounts)
    to_account_exists = any(account['account_id'] == to_account for account in accounts)
    
    if from_account_exists and to_account_exists:
        new_transaction = {
            "transaction_id": len(transactions) + 1,
            "from_account": from_account,
            "to_account": to_account,
            "amount": amount,
        }
        transactions.append(new_transaction)
        return jsonify(new_transaction), 201
    else:
        return "One or more accounts not found", 400


if __name__ == '__main__':
    app.run(debug=True , port=5003)

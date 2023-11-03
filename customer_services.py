from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for customers
customers = [
    {"customer_id": 1, "name": "Vishal Singh"},
    {"customer_id": 2, "name": "Riya Pandey"},
]



############################################## C U S T O M E R #################################

# Get all customers
@app.route('/customers', methods=['GET'])
def get_all_customers():
    return jsonify(customers)

# Update an existing customer
@app.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    data = request.get_json()
    for customer in customers:
        if customer['customer_id'] == customer_id:
            customer['name'] = data.get("name", customer['name'])
            return jsonify(customer)
    return "Customer not found", 404

# Delete an existing customer
@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    for customer in customers:
        if customer['customer_id'] == customer_id:
            customers.remove(customer)
            return "Customer deleted", 200
    return "Customer not found", 404
    
# Get customer details
@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    for customer in customers:
        if customer['customer_id'] == customer_id:
            return jsonify(customer)
    return "Customer not found", 404

# Create a new Customer
@app.route('/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    new_customer = {
        "customer_id": len(customers) + 1,
        "name": data.get("initial_name", 0)
    }
    customers.append(new_customer)
    return jsonify(new_customer), 201

if __name__ == '__main__':
    app.run(debug=True , port=5002)
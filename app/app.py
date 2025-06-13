from flask import Flask, request, jsonify

app = Flask(__name__)

products = []

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)


@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.get_json()
    products.append(data)
    return '', 201


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

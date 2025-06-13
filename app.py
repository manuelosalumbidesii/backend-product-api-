from flask import Flask, request, jsonify

app = Flask(__name__)

products = []

@app.route("/api/products", methods=["GET"])
def get_products():
    return jsonify(products)

@app.route("/api/products", methods=["POST"])
def add_product():
    data = request.json
    product = {
        "id": len(products) + 1,
        "name": data["name"],
        "price": data["price"],
        "stock": data["stock"]
    }
    products.append(product)
    return jsonify(product), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

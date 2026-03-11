from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Calculator API is running!"

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    operation = data.get("operation")
    x = data.get("x")
    y = data.get("y")

    if not operation or x is None or y is None:
        return jsonify({"error": "Missing parameters"}), 400

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        return jsonify({"error": "Invalid numbers"}), 400

    result = None
    if operation == "add":
        result = x + y
    elif operation == "subtract":
        result = x - y
    elif operation == "multiply":
        result = x * y
    elif operation == "divide":
        if y == 0:
            return jsonify({"error": "Division by zero"}), 400
        result = x / y
    else:
        return jsonify({"error": "Unsupported operation"}), 400

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

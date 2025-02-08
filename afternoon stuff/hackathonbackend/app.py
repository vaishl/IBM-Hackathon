from flask import Flask, jsonify, request
import csv
from flask_cors import CORS



app = Flask(__name__)
csv_file = "values.csv"
CORS(app)

# Function to add a new purchase entry
def add_purchase(item, category, carbon_value):
    with open(csv_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([item, category, carbon_value])


# API to add purchase via frontend
@app.route("/add", methods=["POST"])
def add_entry():
    data = request.json
    item = data.get("item")
    category = data.get("category")
    carbon_value = data.get("carbon_value")

    if item and category and carbon_value:
        add_purchase(item, category, carbon_value)
        return jsonify({"message": "Entry added successfully"}), 201
    return jsonify({"error": "Missing data"}), 400


# API to read purchases
@app.route("/purchases", methods=["GET"])
def read_purchases():
    purchases = []
    try:
        with open(csv_file, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:
                    purchases.append({"item": row[0], "category": row[1], "carbon_value": row[2]})
    except FileNotFoundError:
        return jsonify({"error": "No data available"}), 404

    return jsonify(purchases)


if __name__ == "__main__":
    app.run(debug=True)

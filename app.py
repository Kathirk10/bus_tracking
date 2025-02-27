from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Enable CORS for frontend requests

bus_location = {"latitude": 37.7749, "longitude": -122.4194}  # Default to valid location

@app.route('/update_location', methods=['POST'])
def update_location():
    global bus_location
    data = request.json
    if not data or "latitude" not in data or "longitude" not in data:
        return jsonify({"error": "Invalid data"}), 400

    bus_location["latitude"] = data["latitude"]
    bus_location["longitude"] = data["longitude"]

    print("Received location update:", bus_location)  # Debugging log

    return jsonify({"message": "Location updated", "bus_location": bus_location}), 200

@app.route('/get_location', methods=['GET'])
def get_location():
    print("Sending bus location:", bus_location)  # Debugging log
    return jsonify(bus_location), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Run Flask on all network interfaces

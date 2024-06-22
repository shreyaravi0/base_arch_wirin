from flask import Blueprint, jsonify, request

lighting_ac = Blueprint('lighting_ac', __name__)

@lighting_ac.route('/lighting/set', methods=['POST'])
def set_lighting():
    data = request.json
    intensity = data.get('intensity')
    if intensity is None:
        return jsonify({"error": "Lighting intensity is required"}), 400
    result = f"Setting lighting intensity to {intensity}"
    return jsonify({"result": result})

@lighting_ac.route('/ac/set', methods=['POST'])
def set_ac():
    data = request.json
    temperature = data.get('temperature')
    if temperature is None:
        return jsonify({"error": "AC temperature is required"}), 400
    result = f"Setting AC temperature to {temperature}°C"
    return jsonify({"result": result})

from flask import Blueprint, jsonify, request
current_intensity = 0
current_temperature = 0

lighting_ac = Blueprint('lighting_ac', __name__)

@lighting_ac.route('/lighting/set', methods=['POST'])
def set_lighting():
    data = request.json
    intensity = data.get('intensity')
    if intensity is None:
        return jsonify({"error": "Lighting intensity is required"}), 400
    current_intensity = intensity
    result = f"Setting lighting intensity to {intensity}"
    return jsonify({"result": result})

@lighting_ac.route('/lighting/intensity', methods=['GET'])
def get_lighting_intensity():
    return jsonify({"intensity": current_intensity})

@lighting_ac.route('/ac/set', methods=['POST'])
def set_ac():
    data = request.json
    temperature = data.get('temperature')
    if temperature is None:
        return jsonify({"error": "AC temperature is required"}), 400
    result = f"Setting AC temperature to {temperature}°C"
    return jsonify({"result": result})
@lighting_ac.route('/ac/temperature', methods=['GET'])
def get_ac_temperature():
    return jsonify({"temperature": current_temperature})
from flask import Flask, jsonify, request

app = Flask(__name__)

events = []

@app.route('/')
def home():
    return jsonify({"message": "Bienvenido al servicio de autenticación"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

@app.route('/events', methods=['POST'])
def create_event():
    event_data = request.json
    event_data['id'] = len(events) + 1
    events.append(event_data)
    return jsonify(event_data), 201

@app.route('/events', methods=['GET'])
def get_events():
    return jsonify(events), 200

@app.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = next((event for event in events if event['id'] == event_id), None)
    if event is None:
        return jsonify({'error': 'Event not found'}), 404
    return jsonify(event), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
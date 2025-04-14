from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key' 
jwt = JWTManager(app)

# Simulación de base de datos
users_db = {}

@app.route('/')
def home():
    return jsonify({"message": "Bienvenido al servicio de autenticación"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')

    if username in users_db:
        return jsonify({"msg": "Usuario ya existe"}), 400

    users_db[username] = generate_password_hash(password)
    return jsonify({"msg": "Usuario registrado exitosamente"}), 201

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user_password = users_db.get(username)
    if user_password and check_password_hash(user_password, password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Credenciales inválidas"}), 401

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
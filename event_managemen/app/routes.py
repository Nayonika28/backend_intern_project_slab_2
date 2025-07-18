from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Event, Registration
from . import db

main_bp = Blueprint('main', __name__, url_prefix='/')

# ✅ Route: Register User (Admin/User)
@main_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')

    if not all([username, password, role]):
        return jsonify({"message": "Username, password, and role are required"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"message": "User already exists"}), 409

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password_hash=hashed_password, role=role)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

# ✅ Route: Login
@main_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not all([username, password]):
        return jsonify({"message": "Username and password are required"}), 400

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({"message": "Invalid credentials"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

# ✅ Route: Create Event (Only Admins)
@main_bp.route('/events', methods=['POST'])
@jwt_required()
def create_event():
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user).first()

    if not user or user.role != 'admin':
        return jsonify({"message": "Admin access required"}), 403

    data = request.get_json()
    event = Event(
        title=data.get('title'),
        description=data.get('description'),
        date=data.get('date'),
        time=data.get('time'),
        location=data.get('location'),
        capacity=data.get('capacity')
    )
    db.session.add(event)
    db.session.commit()

    return jsonify({"message": "Event created successfully!"}), 201

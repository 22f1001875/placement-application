from flask import Blueprint, request, jsonify, session
from flask_security.utils import hash_password, verify_password
from models.security import User
from flask import current_app
from config import db

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400
    user = User.query.filter_by(email=email).first_or_404()
    print("PASSWORD RECEIVED:", password)
    print("PASSWORD LENGTH:", len(password.encode("utf-8")))
    print("Stored password:", user.password)
    print("Stored length:", len(user.password))
    if verify_password(password, user.password):
        return jsonify({"message": "Login successful", "id": user.id, "token": user.get_auth_token(), "email": email})
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")
    role = data.get("role")
    active = data.get("active", True)

    if not email or not password or role not in ["student", "company"]:
        return jsonify({"message": "Invalid email, password, or role"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"message": "Email already registered"}), 400

    if role == "company":
        active = False

    datastore = current_app.datastore

    user = datastore.create_user(
        email=email,
        password=hash_password(password),
        active=active,
        roles=[role]
    )

    db.session.commit()

    return jsonify({
        "message": "Registration successful",
        "id": user.id,
        "email": email
    }), 201
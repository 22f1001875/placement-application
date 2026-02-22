from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///placement_portal.sqlite3'
    SECRET_KEY = "dev-secret-key"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False
    SECURITY_PASSWORD_HASH = "bcrypt"
    SECURITY_PASSWORD_SALT = "dev-password-salt"
    SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Token"

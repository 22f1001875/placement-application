from flask import Flask
from flask_security import Security, SQLAlchemyUserDatastore
from config import db, BaseConfig
import models
from models import User, Role


def create_app():
    app = Flask(__name__)
    app.config.from_object(BaseConfig)

    db.init_app(app)

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)

    with app.app_context():
        db.create_all()

        for role_name in ["admin", "student", "company"]:
            if not user_datastore.find_role(role_name):
                user_datastore.create_role(name=role_name)

        db.session.commit()

        if not user_datastore.find_user(email="admin@placement.com"):
            admin_user = user_datastore.create_user(
                email="admin@placement.com",
                password="admin123",
                fs_uniquifier="admin_unique"
            )
            user_datastore.add_role_to_user(admin_user, "admin")
            db.session.commit()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

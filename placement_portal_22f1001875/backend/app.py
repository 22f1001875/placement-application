from flask import Flask
from flask_security import Security, SQLAlchemyUserDatastore
from config import db, BaseConfig
import models
from resources import auth_bp
from flask_security.utils import hash_password
from models import User, Role


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
def create_app():
    app = Flask(__name__)
    app.config.from_object(BaseConfig)
    app.datastore = user_datastore #can export as app.datastore to use in other modules
    db.init_app(app)
    security = Security(app, user_datastore)
    app.register_blueprint(auth_bp)
    with app.app_context():
        db.create_all()
        for role_name in ["admin", "student", "company"]:
            if not user_datastore.find_role(role_name):
                user_datastore.create_role(name=role_name)

        db.session.commit()

        if not user_datastore.find_user(email="admin@placement.com"):
            admin_user = user_datastore.create_user(
                email="admin@placement.com",
                password=hash_password("admin123"),
                fs_uniquifier="admin_unique"
            )
            user_datastore.add_role_to_user(admin_user, "admin")
            db.session.commit()
        

    return app


app = create_app()
if __name__ == "__main__":
    app.run(debug=True)

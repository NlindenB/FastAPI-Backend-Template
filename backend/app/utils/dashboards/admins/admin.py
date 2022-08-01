import fastapi as f
import sqladmin as sad

from app.database.db import database


def initialize_sqladmin(app: f.FastAPI) -> sad.Admin:
    admin = sad.Admin(app=app, engine=database.ENGINE)
    # admin.register_model(model=)
    return admin

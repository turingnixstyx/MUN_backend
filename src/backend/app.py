from flask import Flask
import os
from . import config as cf

app = Flask(__name__)
env = os.getenv("FLASK_ENV", "development")

if env == "production":
    app.config.from_object(cf.ProductionConfig)

else:
    app.config.from_object(cf.DevelopmentConfig)
    if app.config["DEBUG"]:
        print("Debug env is on")

    print(app.config["PORT"])


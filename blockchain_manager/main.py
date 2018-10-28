from flask import Flask

from blockchain_manager import http_handler

if __name__ == "__main__":
    app = Flask(__name__)

    app.register_blueprint(http_handler)

    app.run(host="0.0.0.0", port="5303")

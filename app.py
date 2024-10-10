from flask import Flask

from blueprints.init_bp import init_blueprint


app = Flask(__name__)

# app.register_blueprint(car_blueprint, url_prefix='/cars')
app.register_blueprint(init_blueprint, url_prefix='/init')


if __name__ == '__main__':
    app.run()

from flask import Flask

from blueprints.crashes_bp import crashes_blueprint
from blueprints.init_bp import init_blueprint


app = Flask(__name__)

app.register_blueprint(crashes_blueprint)
app.register_blueprint(init_blueprint, url_prefix='/init')


if __name__ == '__main__':
    app.run()

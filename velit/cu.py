# app.py
from flask import Flask
import config

app = Flask(__name__)

# Choose the configuration based on the environment
environment = 'development'  # This could be dynamically set
if environment == 'production':
    app.config.from_object(config.ProductionConfig)
elif environment == 'testing':
    app.config.from_object(config.TestingConfig)
else:
    app.config.from_object(config.DevelopmentConfig)

@app.route('/')
def home():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@postgres:5432/{os.getenv('POSTGRES_DB')}"

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)

@app.route('/')
def home():
    return jsonify({"message": "Flask app is running on Minikube!"})

@app.route('/db_check')
def db_check():
    try:
        db.session.execute("SELECT 1")  # Simple query to check DB
        return jsonify({"message": "Connected to PostgreSQL!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

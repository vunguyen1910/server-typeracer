from flask import Flask,jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
CORS(app)
db = SQLAlchemy(app)

app.secret_key = 'secrect'
app.config['SQLALCHEMY_DATABASE_URI'] = 'DATABASE_URL'

mirgrate = Migrate(app, db)

class Score(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    wpm = db.Column(db.Integer)
    time = db.Column(db.Float)
    errors = db.Column(db.Integer)
    excerpt_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)

class Excerpt(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.Text)

db.create_all()

@app.route("/")
def root():
    return jsonify([
        'hello', 'world'
    ])
@app.route('/excerpts')
def lists():
    return jsonify([
        "The enormous room on the ground floor faced",
    ])

@app.route('/scores', methods=['POST','GET'])
def create():
    dt = request.get_json()
    score = Score(user_id = 1, time = dt['time'], wpm = dt['wpm'], errors=dt['errorCount'],excerpt_id = 1)
    db.session.add(score)
    db.session.commit()
    return jsonify({'id': score.id, 'time': score.time, 'wpm': score.wpm, 'errors':score.errors})

if __name__ == "__main__":
    app.run(debug=True)
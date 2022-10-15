from flask import Flask, request, render_template, url_for, jsonify, redirect, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://efuraimujs:root@localhost:5432/quotesappdb'
# silence the deprecation warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class FavQuotes(db.Model):
    qt_id = db.Column(db.Integer, primary_key=True)
    qt_detail = db.Column(db.String(2000))
    qt_author = db.Column(db.String(30))


@app.route('/')
def index():
    billions = ['Elon Musk', 'Bernard Arnault & family', 'Jeff Bezos']
    return render_template('index.html', quote='', billions=billions)


@app.route('/about')
def about():
    return '<b><h1>About Page</h1></b>'


@app.route('/fav_quotes')
def fav_quotes():
    query_results = FavQuotes.query.all()
    return render_template('quotes.html', query_results=query_results)


@app.route('/reg_quotes')
def reg_quotes():

    return render_template('reg-quotes.html')


@app.route('/process_quote', methods=['POST'])
def process_quote():
    qt_author = request.form['qt_author']
    qt_detail = request.form['qt_detail']
    qt_data = FavQuotes(qt_author=qt_author, qt_detail=qt_detail)
    db.session.add(qt_data)
    db.session.commit()
    return redirect(url_for('index'))

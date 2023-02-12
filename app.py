from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), primary_key=False)
    intro = db.Column(db.String(300), primary_key=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/posts')
def posts():
    articles = Task.query.order_by(Article.date.desc()).all()
    return render_template("posts.html", articles=articles)


@app.route('/posts/<int:id>')
def post_detail(id):
    task = Task.query.get(id)
    return render_template("post_detail.html", article=article)


@app.route('/posts/<int:id>/del')
def post_delete(id):
    task = Task.query.get_or_404(id)

    try:
        db.session.delete(task)
        db.session.commit()
        return redirect('/posts')
    except:
        return "Oшибка"

@app.route('/create-article', methods=['GET'])
def create_article():
    if request.method== 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']
        title= Task(title=title,intro=intro, text=text)
        try:
            db.session.add(task)
            db.session.commit()
            return redirect('/posts')
        except:
            return "Oшибка "

    else:
        return render_template ("create-article.html")
    
    elif:

@app.route('/create-article', methods=['POST'])
def create_article():
    if request.method== 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']
        title= Task(title=title,intro=intro, text=text)
        try:
            db.session.add(task)
            db.session.commit()
            return redirect('/posts')
        except:
            return "Oшибка "

    else:
        return render_template ("create-article.html")

@app.route('/posts/<int:id>/update', methods=['PUT'])
def post_update(id):
    task = Task.query.get(id)
    if request.method== 'POST':
        task.title = request.form['title']
        task.intro = request.form['intro']
        task.text = request.form['text']

        try:
            db.session.commit()
            return redirect('/posts')
        except:
            return "Oшибка "

    else:
        return render_template ("post_update.html", task=task)



if __name__ == "__main__":
    app.run(debug=True)
   
\n

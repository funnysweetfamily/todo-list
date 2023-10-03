from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'
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



@app.route('/tasks')
def posts():
    tasks = Task.query.order_by(Task.date.desc()).all()
    return render_template("tasks.html", tasks=tasks)


@app.route('/tasks/<int:id>')
def post_detail(id):
    task = Task.query.get(id)
    return render_template("post_detail.html", task=task)


@app.route('/tasks/<int:id>/del', methods=['POST','GET'])
def post_delete(id):
    task = Task.query.get_or_404(id)

    try:
        db.session.delete(task)
        db.session.commit()
        return redirect('/tasks')
    except:
        return "Oшибка"

@app.route('/tasks/publish', methods=['POST','GET'])
def create_task():
    if request.method== 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']
        task = Task(title=title,intro=intro, text=text)
        try:
            db.session.add(task)
            db.session.commit()
            return redirect('/tasks')
        except:
            return "Oшибка "

    else:
        return render_template ("create-task.html")

@app.route('/tasks/<int:id>/change', methods=['POST','GET'])
def post_update(id):
    task = Task.query.get(id)
    if request.method== 'POST':
        task.title = request.form['title']
        task.intro = request.form['intro']
        task.text = request.form['text']

        try:
            db.session.commit()
            return redirect('/tasks')
        except:
            return "Oшибка "

    else:
        return render_template ("post_update.html", task=task)



if __name__ == "__main__":
    app.run(debug=True)

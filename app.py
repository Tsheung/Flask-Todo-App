from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):    
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

@app.route('/')
def index():
    list_to = Todo.query.all()
    print(list_to)
    return render_template("base.html", list_to=list_to)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        new_todo = Todo(title="todo 1 ", complete=False)
        db.session.add(new_todo)
        db.session.commit()

    app.run(debug=True)
import sqlite3
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
DATABASE = 'students.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                registration_number TEXT NOT NULL
            )
        ''')
        conn.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    registration_number = request.form['registration_number']
    
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('INSERT INTO students (name, registration_number) VALUES (?, ?)', 
                     (name, registration_number))
        conn.commit()
    
    return redirect(url_for('index'))

@app.route('/class_list')
def class_list():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.execute('SELECT * FROM students')
        students = cursor.fetchall()
    
    return render_template('class_list.html', students=students)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

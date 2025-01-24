# Class List Population System

from flask import Flask, request, render_template, redirect, url_for
import csv

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    reg_number = request.form['reg_number']
    
    with open('class_list.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, reg_number])
    
    return redirect(url_for('thank_you'))

# Route for thank you page
@app.route('/thank_you')
def thank_you():
    return "Thank you for submitting your information!"

if __name__ == '__main__':
    app.run(debug=True)

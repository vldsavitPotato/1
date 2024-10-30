from flask import Flask, render_template

app = Flask(__name__)

def say_hello(name):
  return f"Hello, {name}!"

@app.route("/")
def index():
  return render_template('index.html', 
                         say_hello=say_hello)

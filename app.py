from flask import Flask, render_template
from face_detecter import detector


app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/')
def my_link():
  cam = detector()
  return "Thank You"

if __name__ == '__main__':
  app.run(debug=True)

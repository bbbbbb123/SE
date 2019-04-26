from flask import *
#from waitress import *
from datetime import datetime
import Calculator as calculator
app = Flask(__name__)

#serve(app, host='127.0.0.1', port=8080)

@app.route('/')

def index():
    data = "Deploying a Flask App To Heroku"
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

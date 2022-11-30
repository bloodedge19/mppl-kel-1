from config import *
from db import *
from controller import *
from routes import *
from hr import *
from flask_cors import CORS

CORS(app)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['Access-Control-Allow-Origin'] = '*' 
    return response

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",threaded=True)
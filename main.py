from flask import Flask
from flask import request
from handlers.api_handler import API_OBJECT


app = Flask(__name__)


@app.route("/cars")
def APIHandler():
    """Handles requests via the API object"""

    method = request.json['method']

    if method in API_OBJECT["GET"]:
        return API_OBJECT["GET"][method]()
    
    return "Method specified in arguments not recognised"


if __name__ == '__main__':
    # run app in debug mode on port 80
    app.run(debug=True, port=8080)

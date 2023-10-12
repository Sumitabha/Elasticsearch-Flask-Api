from flask import Flask
from flask_cors import CORS
import searchEmployees

app = Flask(__name__)
CORS(app)

app.add_url_rule('/getEmployees', view_func=searchEmployees.getEmployees, methods=['GET'])

if __name__ == '__main__':
   app.run(port=5000)
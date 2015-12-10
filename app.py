from flask import Flask, render_template
from parser import SwaggerParser

app = Flask(__name__)

parser = SwaggerParser("spec.yaml")

@app.route("/")
def index():
     return render_template('index.html', operations = parser.paths())

if __name__ == '__main__':
    app.run(debug=True)

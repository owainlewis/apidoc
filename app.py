from flask  import Flask, render_template
from parser import SwaggerParser

app = Flask(__name__)

parser = SwaggerParser("static/specs/examples.yaml")

@app.route("/")
def index():
     return render_template('index.html', spec = parser.data, operations = parser.operations())

if __name__ == '__main__':
    app.run(debug=True)

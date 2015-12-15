import os
from flask  import Flask, render_template
from parser import SwaggerParser

app = Flask(__name__)

parser = SwaggerParser("static/specs/examples.yaml")

@app.route("/")
def index():
     return render_template('index.html', spec = parser.data, operations = parser.operations())

PORT = os.getenv('VCAP_APP_PORT', '5000')

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(PORT))

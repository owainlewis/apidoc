import os

from flask  import Flask, render_template
from parser import SwaggerParser
from os import listdir
from os.path import isfile, join

app = Flask(__name__)

SPEC_PATH = "static/specs"

def spec_exists(spec):
     return isfile(join(SPEC_PATH, spec))

def load_specs():
     return [f.replace('.yaml','') for f in listdir(SPEC_PATH) if spec_exists(f)]

@app.route("/docs/<name>")
def spec(name):
     parser = SwaggerParser("static/specs/%s.yaml" % name)
     return render_template('spec.html', spec = parser.spec, paths = parser.paths())

@app.route("/")
def index():
    return render_template('intro.html', specs=load_specs())

PORT = int(os.getenv('PORT', '5000'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)

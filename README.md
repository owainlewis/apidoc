# API DOC

Generate professional looking, human readable documentation from Swagger.

A demo can be found [here](https://swagger-docs.herokuapp.com/docs/uber)

Currently this only supports Swagger YAML format, but RAML will be next. You can
quickly customize any of the templates.

Simply drop your Swagger specs in static/specs and off you go :)

![](https://raw.githubusercontent.com/owainlewis/apidoc/master/static/images/preview.png)

## Getting Started

This app can use either Python 2 or 3 and is pretty much a standard
Flask application.

```bash
# Install deps
sudo apt-get install python3-pip
pip3 install -r requirements.txt
# Run it
python3 app.py
# Visit localhost:5000
```

Update the templates or stylesheets to suite your needs.

## Deploy to Heroku

```bash
heroku create mydocs
git push heroku master
```

# License

You are free to use this for whatever you want. Do whatever you like
with it :)

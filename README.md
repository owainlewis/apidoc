# APIDOC (WIP)

Generate professional looking, human readable documentation from
Swagger or RAML.

A demo can be found [here](https://swagger-docs.herokuapp.com/docs/uber)

Currently this only supports Swagger but RAML will be next. You can
quickly customize any of the templates.

Simply drop your Swagger specs in static/specs and off you go :)

## Getting Started

This app can use either Python 2 or 3 and is pretty much a standard
Flask application.

```
# Install deps
pip3 install -r requirements.txt
# Run it
python app.py
# Visit localhost:5000
```

Update the templates or stylesheets to suite your needs.

## Deploy to Heroku

```
heroku create mydocs
git push heroku master
```

# Preview

![](https://raw.githubusercontent.com/owainlewis/apidoc/master/static/images/prev.png)

# License

You are free to use this for whatever you want. Do whatever you like
with it :)

from flask import Flask, render_template
from flask import jsonify
from flask import request

# [START gae_python37_datastore_store_and_fetch_times]



# [END gae_python37_datastore_store_and_fetch_times]
app = Flask(__name__)

# morningData = tryGotUnassignedInResponse2(date,session,street)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.

    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)

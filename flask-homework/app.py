from flask import Flask
import logging


app = Flask(__name__)


@app.route('/hello')
def hello():
    logging.info('Here is logging info')
    return 'Hello, world!'


app.run()

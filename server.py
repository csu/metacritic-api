#!/usr/bin/env python
from flask import Flask, jsonify, request
from quora import Quora, Activity

app = Flask(__name__)

# log to stderr
import logging
from logging import StreamHandler
file_handler = StreamHandler()
app.logger.setLevel(logging.DEBUG)
app.logger.addHandler(file_handler)

####################################################################
# Routes
####################################################################

@app.route('/', methods=['GET'])
def index_route():
    return jsonify({
        'author': 'Christopher Su',
        'author_url': 'http://christopher.su',
        'base_url': 'http://metacritic-api.herokuapp.com',
        'project': 'Quora API',
        'project_url': 'https://github.com/csu/metacritic-api',
        'project_documentation': 'http://christopher.su/metacritic-api/',
        'project_issues': 'https://github.com/csu/metacritic-api/issues',
        'endpoints': {
            
        }
    })

@app.route('/users/<user>', methods=['GET'])
def user_stats_route(user):
    return jsonify(Quora.get_user_stats(user))

####################################################################
# Start Flask
####################################################################
if __name__ == '__main__':
    app.run(debug=True)

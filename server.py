#!/usr/bin/env python
from flask import Flask, jsonify, request
import metacritic

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
        'project': 'Metacritic API',
        'project_url': 'https://github.com/csu/metacritic-api',
        'project_documentation': 'http://christopher.su/metacritic-api/',
        'project_issues': 'https://github.com/csu/metacritic-api/issues',
        'endpoints': {
            'Get all critics.', '/critics',
            'Get critics by letter.', '/critics/letter/<letter>',
            'Get reviews by critic.', '/critics/<critic_slug>'
        }
    })

@app.route('/critics', methods=['GET'])
def all_critics():
    return jsonify({'critics': metacritic.get_all_movie_critics()})

@app.route('/critics/letter/<letter>', methods=['GET'])
def critics_by_letter(letter):
    return jsonify({'critics': metacritic.get_movie_critics_for_letter(letter)})

@app.route('/critics/<critic_slug>', methods=['GET'])
def critic_by_slug(critic_slug):
    return jsonify(metacritic.get_movie_critic(critic_slug))

####################################################################
# Start Flask
####################################################################
if __name__ == '__main__':
    app.run(debug=True)

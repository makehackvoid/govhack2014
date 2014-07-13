from govhack2014 import app
from flask import render_template, request, flash, redirect, url_for, jsonify  # noqa
from twitter import Twitter


def get_post_value(key):
    try:
        return request.form[key]
    except KeyError:
        return None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data/artsact.json')
def artsact():
    return app.send_static_file('artsact.json')


@app.route('/ambient')
def ambient():
    return render_template('ambient.html')


@app.route('/twitter/latest_request')
def twitter_latest_request():
    t = Twitter()
    last_tweet = t.get_suburb()
    print('\n\nlast tweet:', last_tweet, '\n\n')
    return jsonify(**last_tweet)

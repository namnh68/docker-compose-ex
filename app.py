#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from flask import Flask
from redis import Redis

redis_host = os.getenv('REDIS_HOST', "redis")
redis_port = os.getenv('REDIS_PORT', 6379)

app = Flask(__name__)
redis = Redis(host=redis_host, port=redis_port)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello World! I have been seen {0} times'.format(redis.get('hits'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

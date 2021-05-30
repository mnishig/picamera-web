# raspi camera web app
# streaming;
#   mjpeg-streamer or ustremer
# web framework:
#   bottle
#

import io
import json
import re
import socket
import time
import urllib.request
import urllib.parse

from bottle import (
    Bottle, 
    response,
    run,
    static_file,
    template
)

# initialize 
with open('config.json', 'r') as f:
    conf = json.load(f)

HOST = conf['Host']
PORT = conf['Port']
SNAPSHOT_URL = conf['SnapshotURL']
STREAM_URL = conf['StreamURL']
TEMPLATE = conf['Template']
DEBUG = conf['Debug']

app = Bottle()
# end of initialize

def get_filename():
    """
    return YYYYMMDD-HHmmss (HH:0-23)
    """
    t = time.time()
    lt = time.localtime(t)
    st = time.strftime('%Y%m%d-%H%M%S',lt)
    return st

def url_convert_ip():
    token = urllib.parse.urlparse(conf['StreamURL'])
    (ip, port) = token.netloc.split(':')
    ip = socket.gethostbyname(ip)
    url = '{}://{}:{}{}?{}'.format(token.scheme, ip, port, token.path, token.query)
    return url


@app.route('/')
def index():
    url = url_convert_ip()
    print('url: '+ url)
    return template(TEMPLATE, root='./', stream_url=url)

@app.route('/snapshot')
def take():
    print('/take: start...')

    req = urllib.request.Request(SNAPSHOT_URL)
    with urllib.request.urlopen(req) as res:
        data = res.read()

        if data:
            with open(get_filename()+ '.jpg', 'wb') as f:
                f.write(data)

    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return json.dumps({"ret": "take picture"})


app.run(host=HOST, port=PORT, debug=DEBUG)

# end of file

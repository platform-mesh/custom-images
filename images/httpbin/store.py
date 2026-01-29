import os
import io
from .core import app, request, make_response

@app.route('/files/<string:filename>', methods=[ 'POST', 'PUT' ])
def store(filename):
    """ Store a file.
    ---
    tags:
        - HTTP Method
    produces:
        - application/json
    responses:
      200:
        description: File has been stored.
    """
    outpath = os.path.join(os.environ.get('DATA_DIR', '/tmp'), filename)
    with io.open(outpath, 'wb') as f:
        f.write(request.data)
    response = make_response()
    response.status_code = 200
    return response

@app.route('/files/<string:filename>', methods=[ 'GET' ])
def retrieve(filename):
    """ Retrieve a file.
    ---
    tags:
        - HTTP Method
    produces:
        - application/json
    responses:
      200:
        description: The file has been found and is returned.
    """
    import json
    import base64
    response = make_response()
    readpath = os.path.join(os.environ.get('DATA_DIR', '/tmp'), filename)
    if not os.path.exists(readpath):
        response.status_code = 404
        response.data = 'File does not exist'
        return response

    with io.open(readpath, 'rb') as f:
        file_data = f.read()

    accept = request.headers.get('Accept', 'application/octet-stream')
    if 'application/json' in accept:
        try:
            decoded = file_data.decode('utf-8')
            json_data = json.loads(decoded)
            response.data = json.dumps(json_data)
        except Exception:
            response.data = json.dumps({'data': base64.b64encode(file_data).decode('utf-8')})
        response.content_type = 'application/json'
    else:
        response.data = file_data
        response.content_type = 'application/octet-stream'
    response.status_code = 200
    return response

from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy(path):
    url = f"http://localhost:5000/{path}"
    headers = {key: value for key, value in request.headers.items() if key.lower() != 'host'}
    headers['X-Custom-Header'] = 'YourCustomHeaderValue'

    response = requests.request(
        method=request.method,
        url=url,
        headers=headers,
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False
    )

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in response.raw.headers.items()
               if name.lower() not in excluded_headers]

    response = Response(response.content, response.status_code, headers)
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

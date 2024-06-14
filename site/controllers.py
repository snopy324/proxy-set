from flask import request, render_template

def setup_routes(app):
    @app.route('/headers')
    def headers():
        headers = dict(request.headers)
        return render_template('headers.html', headers=headers)

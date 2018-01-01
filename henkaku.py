from flask import Flask, request, send_from_directory
app = Flask(__name__)

@app.route('/go/')
def go():
    return send_from_directory('static', 'index.html')

@app.route('/go/<path:path>')
def go_payload(path):
    return send_from_directory('static', path)

@app.route('/')
def root():
    return '<html><body>Here we <a href="/go">go</a></body></html>'

app.run('0.0.0.0', 80)

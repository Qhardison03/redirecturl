from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the OAuth2.0 Demo!'


@app.route('/callback')
def callback():
    code = request.args.get('code')
    state = request.args.get('state')
    return f"Authorization code: {code}, State: {state}"

if __name__ == '__main__':
    app.run(debug=True)
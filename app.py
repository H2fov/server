from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    tips = [
        {'title': 'Truth1', 'content': 'manya is stupid'},
        {'title': 'Truth2', 'content': 'many plays cod'},
        {'title': 'Truth3', 'content': 'manya is baka'}
    ]
    return render_template('index.html', tips=tips)

if __name__ == '__main__':
    host = '0.0.0.0'  # Replace with your desired host
    port = 8080  # Replace with your desired port
    app.run(host=host, port=port)

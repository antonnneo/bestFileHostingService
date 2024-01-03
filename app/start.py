from flask import Flask
app = Flask(__name__)

@app.route('/new')
def new_note():
    return 'Привет, мир!'

if __name__ == '__main__':
    app.run(debug=False, port=5000, host="0.0.0.0")
from flask import Flask, render_template


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inquiry')
def inquiry():
    return render_template('inquiry.html')

if __name__ == '__main__':
    app.run(debug=True)
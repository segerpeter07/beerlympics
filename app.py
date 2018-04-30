from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(host='35.227.23.25', port="5000")

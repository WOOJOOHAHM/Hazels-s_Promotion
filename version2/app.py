from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

@app.route('/')
def about():
    return render_template('template.html')

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000)
    app.run(host='0.0.0.0')
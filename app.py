from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']
    return f"Сәлем, {name}! Сенің хабарламаң: {message}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/compare-rythm')
def compare_rythm():
    return render_template('compare_rythm.html')


@app.route('/test-intonation')
def test_intonation():
    return render_template('test_intonation.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/ictf/")
def ictf():
    return render_template('ictf.html')

@app.route("/netzwerk/")
def netzwerk():
    return render_template('netzwerk.html')

@app.route("/wlan/")
def wlan():
    return render_template('wlan.html')

@app.route("/proxychains/")
def proxychains():
    return render_template('proxychains.html')

@app.route("/bufferoverflow/")
def bufferoverflow():
    return render_template('bufferoverflow.html')

if __name__ == "__main__":
    app.run(debug=True)

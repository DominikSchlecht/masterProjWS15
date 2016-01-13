from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

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

@app.route("/xss/")
def xss():
    return render_template('xss.html')

@app.route("/nmap/")
def nmap():
    return render_template('nmap.html')

@app.route("/burpsuite/")
def burpsuite():
    return render_template('burpsuite.html')

@app.route("/commandinjection/")
def commandinjection():
    return render_template('commandinjection.html')

if __name__ == "__main__":
    app.run(debug=True)

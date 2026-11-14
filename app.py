
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>SUGALI CYBER MAP</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
    background: #050b16;
    color: #00ff99;
    font-family: Arial;
    text-align: center;
    padding: 30px;
}
h1 { color: #00ff99; }
a {
    display: inline-block;
    padding: 15px 25px;
    background: #00ff99;
    color: #050b16;
    text-decoration: none;
    border-radius: 10px;
    font-weight: bold;
}
</style>
</head>
<body>
<h1>🌍 SUGALI CYBER MAP</h1>
<h3>LIVE CYBER THREAT VISUALIZATION</h3>
<p>Public cyber threat intelligence map</p>
<a href="https://cybermap.kaspersky.com/" target="_blank">
OPEN LIVE CYBER MAP
</a>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

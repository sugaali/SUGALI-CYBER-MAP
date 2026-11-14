from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head><meta name="google-site-verification" content="A4uw38yhALdtNyz7rkYlYTYLx6n1Wpc5B8ZwhqGssgI" />
<title>SUGALI CYBER MAP</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
    background: #050b16;
    color: #00ff99;
    font-family: Arial;
    text-align: center;
}
h1 { color: #00ff99; }
iframe {
    width: 95%;
    height: 75vh;
    border: 2px solid #00ff99;
    border-radius: 12px;
}
</style>
</head>
<body>
<h1>🌍 SUGALI CYBER MAP</h1>
<h3>LIVE CYBER THREAT VISUALIZATION</h3>
<p>Public cyber threat intelligence map</p>
<iframe src="https://cybermap.kaspersky.com/"></iframe>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
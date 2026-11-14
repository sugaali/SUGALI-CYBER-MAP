
from flask import Flask, render_template_string
from flask import make_response

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="google-site-verification" content="A4uw38yhALdtNyz7rkYlYTYLx6n1Wpc5B8ZwhqGssgI">
<title>SUGALI CYBER MAP | Cyber Security</title>
<style>
* { box-sizing: border-box; }
body {
    margin: 0;
    background: #07111f;
    color: #e8f5ff;
    font-family: Arial, sans-serif;
}
header {
    padding: 22px;
    background: #0c1b2e;
    border-bottom: 1px solid #00e6a0;
    text-align: center;
}
header h1 { color: #00e6a0; margin: 0; }
nav { margin-top: 15px; }
nav a {
    color: #b8d5e8;
    margin: 8px;
    text-decoration: none;
}
.hero {
    padding: 65px 20px;
    text-align: center;
}
.hero h2 {
    color: #00e6a0;
    font-size: 32px;
}
.hero p { color: #b8cadd; line-height: 1.7; }
.btn {
    display: inline-block;
    background: #00e6a0;
    color: #07111f;
    padding: 15px 25px;
    border-radius: 8px;
    text-decoration: none;
    font-weight: bold;
    margin-top: 15px;
}
section {
    max-width: 850px;
    margin: 25px auto;
    padding: 25px;
    background: #102238;
    border-radius: 12px;
}
h2 { color: #00e6a0; }
footer {
    text-align: center;
    padding: 25px;
    color: #8da8bc;
}
</style>
</head>
<body>
<header>
<h1>🌍 SUGALI CYBER MAP</h1>
<nav>
<a href="#home">Home</a>
<a href="#learning">Learning</a>
<a href="#security">Security</a>
<a href="#about">About</a>
</nav>
</header>

<div class="hero" id="home">
<h2>Explore The Cyber World</h2>
<p>Learn cybersecurity. Understand digital threats.
Build a safer internet.</p>
<a class="btn"
href="https://cybermap.kaspersky.com/"
target="_blank" rel="noopener noreferrer">
OPEN LIVE CYBER MAP
</a>
</div>

<section id="learning">
<h2>📚 Cyber Security Learning</h2>
<p>Learn ethical hacking, network security,
online safety and digital protection.</p>
</section>

<section id="security">
<h2>🛡️ Security Information</h2>
<p>Understand phishing, malware, strong passwords
and safe internet practices.</p>
</section>

<section id="about">
<h2>👨‍💻 About SUGALI</h2>
<p>SUGALI CYBER MAP is an educational project
focused on cybersecurity awareness and learning.</p>
<p>Our mission is to promote a safer digital world.</p>
</section>

<footer>
<p>© 2026 SUGALI CYBER MAP</p>
<p>Educational Cybersecurity Project</p>
</footer>
</body>
</html>
"""

@app.after_request
def security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "style-src 'self' 'unsafe-inline'; "
        "base-uri 'self'; "
        "form-action 'self'; "
        "frame-ancestors 'none'"
    )
    return response

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

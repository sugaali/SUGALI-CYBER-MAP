
from flask import Flask, render_template_string, request

app = Flask(__name__)

TEXT = {
    "en": {
        "title": "Explore The Cyber World",
        "intro": "Learn cybersecurity. Understand digital threats. Build a safer internet.",
        "button": "OPEN LIVE CYBER MAP",
        "learning": "Cyber Security Learning",
        "learning_text": "Learn ethical hacking concepts, network security, online safety and digital protection.",
        "security": "Security Information",
        "security_text": "Understand phishing, malware, strong passwords and safe internet practices.",
        "password": "Password Safety",
        "password_text": "Use unique passwords and enable two-factor authentication.",
        "phishing": "Phishing Awareness",
        "phishing_text": "Learn how to recognize suspicious links and fake messages.",
        "network": "Network Security",
        "network_text": "Understand how networks work and how to protect your devices.",
        "about": "About SUGALI",
        "about_text": "SUGALI CYBER MAP is a free educational project focused on cybersecurity awareness and learning.",
        "mission": "Our mission is to promote a safer digital world.",
        "free": "FREE CYBERSECURITY LEARNING",
        "home": "Home",
        "nav_learning": "Learning",
        "nav_security": "Security",
        "nav_about": "About",
    },

    "hi": {
        "title": "Cyber Duniya Ko Samjhein",
        "intro": "Cybersecurity seekhein. Digital khatron ko samjhein. Internet ko surakshit banayein.",
        "button": "LIVE CYBER MAP KHOLEN",
        "learning": "Cyber Security Ki Padhai",
        "learning_text": "Ethical hacking ke concepts, network security aur online safety seekhein.",
        "security": "Security Ki Jankari",
        "security_text": "Phishing, malware, majboot password aur internet safety samjhein.",
        "password": "Password Ki Suraksha",
        "password_text": "Har account ke liye alag password rakhein aur two-factor authentication lagayein.",
        "phishing": "Phishing Se Bachav",
        "phishing_text": "Fake messages aur suspicious links ko pehchanna seekhein.",
        "network": "Network Security",
        "network_text": "Network kaise kaam karta hai aur apne devices ko kaise surakshit rakhein.",
        "about": "SUGALI Ke Baare Mein",
        "about_text": "SUGALI CYBER MAP ek muft educational project hai jo cybersecurity ki jankari deta hai.",
        "mission": "Hamara mission digital duniya ko zyada surakshit banana hai.",
        "free": "MUFT CYBERSECURITY SEEKHEIN",
        "home": "Home",
        "nav_learning": "Learning",
        "nav_security": "Security",
        "nav_about": "About",
    }
}

HTML = """
<!DOCTYPE html>
<html lang="{{ lang }}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<meta name="description"
content="SUGALI CYBER MAP - Free Cybersecurity Learning and Online Safety Education">

<meta name="google-site-verification"
content="A4uw38yhALdtNyz7rkYlYTYLx6n1Wpc5B8ZwhqGssgI">

<title>SUGALI CYBER MAP</title>

<style>
* {
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    margin: 0;
    background: #07111f;
    color: #e8f5ff;
    font-family: Arial, sans-serif;
}

header {
    padding: 22px 12px;
    background: #0c1b2e;
    border-bottom: 2px solid #00e6a0;
    text-align: center;
}

header h1 {
    color: #00e6a0;
    font-size: 27px;
}

nav {
    margin-top: 18px;
}

nav a {
    color: #b8d5e8;
    margin: 8px;
    text-decoration: none;
    font-size: 14px;
}

nav a:hover {
    color: #00e6a0;
}

.language {
    margin-top: 20px;
}

.language a {
    display: inline-block;
    padding: 10px 15px;
    border: 1px solid #00e6a0;
    border-radius: 8px;
    color: #00e6a0;
    text-decoration: none;
    margin: 5px;
}

.language a.active {
    background: #00e6a0;
    color: #07111f;
}

.hero {
    padding: 65px 18px;
    text-align: center;
    background: linear-gradient(135deg, #07111f, #102c42);
}

.hero h2 {
    color: #00e6a0;
    font-size: 30px;
}

.hero p {
    color: #b8cadd;
    line-height: 1.8;
}

.hero h3 {
    color: #00e6a0;
}

.btn {
    display: inline-block;
    background: #00e6a0;
    color: #07111f;
    padding: 15px 23px;
    border-radius: 8px;
    text-decoration: none;
    font-weight: bold;
    margin-top: 15px;
}

.btn:hover {
    background: #ffffff;
}

section {
    max-width: 850px;
    margin: 25px auto;
    padding: 25px;
    background: #102238;
    border: 1px solid #1c4057;
    border-radius: 12px;
    width: 92%;
}

section h2 {
    color: #00e6a0;
}

section p {
    color: #c2d5e5;
    line-height: 1.8;
}

footer {
    text-align: center;
    padding: 25px;
    color: #8da8bc;
    background: #0c1b2e;
    margin-top: 35px;
}

@media(max-width: 600px) {
    header h1 {
        font-size: 22px;
    }

    .hero h2 {
        font-size: 25px;
    }

    nav a {
        display: inline-block;
        margin: 7px;
    }
}
</style>
</head>

<body>

<header>

<h1>🌍 SUGALI CYBER MAP</h1>

<div class="language">

<a href="{{ url_for('home', lang='en') }}"
class="{{ 'active' if lang == 'en' else '' }}">
English
</a>

<a href="{{ url_for('home', lang='hi') }}"
class="{{ 'active' if lang == 'hi' else '' }}">
Hindi (English Letters)
</a>

</div>

<nav>
<a href="#home">{{ t.home }}</a>
<a href="#learning">{{ t.nav_learning }}</a>
<a href="#security">{{ t.nav_security }}</a>
<a href="#about">{{ t.nav_about }}</a>
</nav>

</header>

<div class="hero" id="home">

<h2>{{ t.title }}</h2>

<p>{{ t.intro }}</p>

<h3>{{ t.free }}</h3>

<a class="btn"
href="https://cybermap.kaspersky.com/"
target="_blank"
rel="noopener noreferrer">
{{ t.button }}
</a>

</div>

<section id="learning">

<h2>📚 {{ t.learning }}</h2>
<p>{{ t.learning_text }}</p>

</section>

<section id="security">

<h2>🛡️ {{ t.security }}</h2>
<p>{{ t.security_text }}</p>

</section>

<section>

<h2>🔐 {{ t.password }}</h2>
<p>{{ t.password_text }}</p>

</section>

<section>

<h2>🎣 {{ t.phishing }}</h2>
<p>{{ t.phishing_text }}</p>

</section>

<section>

<h2>🌐 {{ t.network }}</h2>
<p>{{ t.network_text }}</p>

</section>

<section id="about">

<h2>👨‍💻 {{ t.about }}</h2>

<p>{{ t.about_text }}</p>

<p>{{ t.mission }}</p>

</section>

<footer>

<p>© 2026 SUGALI CYBER MAP</p>

<p>Free Educational Cybersecurity Project</p>

</footer>

</body>
</html>
"""


@app.after_request
def security_headers(response):

    response.headers["X-Content-Type-Options"] = "nosniff"

    response.headers["X-Frame-Options"] = "DENY"

    response.headers["Referrer-Policy"] = (
        "strict-origin-when-cross-origin"
    )

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

    lang = request.args.get("lang", "en")

    if lang not in TEXT:
        lang = "en"

    return render_template_string(
        HTML,
        lang=lang,
        t=TEXT[lang]
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )

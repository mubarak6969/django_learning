from django.http import HttpResponse

def home(request):
    html = """
    <html>
        <body style="font-family: Arial; text-align: center;
                     background-color: #f0f8ff; padding: 50px;">
            <h1 style="color: #2e86de;">🕌 Assalamu Alaikum!</h1>
            <h2>Welcome to My Django Website</h2>
            <p>Built with Python & Django 5.2!</p>
            <nav>
                <a href="/about/">About</a> &nbsp;|&nbsp;
                <a href="/contact/">Contact</a> &nbsp;|&nbsp;
                <a href="/skills/">Skills</a> &nbsp;|&nbsp;
                <a href="/projects/">Projects</a>
            </nav>
        </body>
    </html>
    """
    return HttpResponse(html)


def about(request):
    html = """
    <html>
        <body style="font-family: Arial; text-align: center;
                     background-color: #fff9f0; padding: 50px;">
            <h1 style="color: #e67e22;">👨‍💻 About Me</h1>
            <p>My name is <strong>Mubarak</strong>.</p>
            <p>I am learning Django and building real websites!</p>
            <p>I am a Django developer! 🚀</p>
            <a href="/">← Back to Home</a>
        </body>
    </html>
    """
    return HttpResponse(html)

def contact(request):
    html = """
    <html>
        <body style="font-family: Arial; text-align: center;
                     background-color: #f0fff0; padding: 50px;">
            <h1 style="color: #27ae60;">📬 Contact Me</h1>
            <p>Email: mubarak@djangolearner.com</p>
            <p>I am learning Django and loving it!</p>
            <a href="/">← Back to Home</a>
        </body>
    </html>
    """
    return HttpResponse(html)


def skills(request):
    html = """
    <html>
        <body style="font-family: Arial; text-align: center;
                     background-color: #fff0f0; padding: 50px;">
            <h1 style="color: #e74c3c;">⚡ My Skills</h1>
            <ul style="list-style: none;">
                <li>🐍 Python</li>
                <li>🌐 Django</li>
                <li>💻 HTML</li>
                <li>🎯 Problem Solving</li>
            </ul>
            <a href="/">← Back to Home</a>
        </body>
    </html>
    """
    return HttpResponse(html)


def projects(request):
    html = """
    <html>
        <body style="font-family: Arial; text-align: center;
                     background-color: #f5f0ff; padding: 50px;">
            <h1 style="color: #8e44ad;">🚀 My Projects</h1>
            <p>🔨 Project 1: My Django Website (this one!)</p>
            <p>🔨 Project 2: Coming soon...</p>
            <p>🔨 Project 3: Coming soon...</p>
            <a href="/">← Back to Home</a>
        </body>
    </html>
    """
    return HttpResponse(html)
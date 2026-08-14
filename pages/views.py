from django.http import HttpResponse
 
def home(request):
    html = """
    <html>
        <body style="font-family: Arial; text-align: center;
                     background-color: #f0f8ff; padding: 50px;">
            <h1 style="color: #2e86de;">Welcome to My Django Portfolio</h1>
            <h2>Full-Stack Web Developer</h2>
            <p>Built with Python & Django 5.2</p>
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
            <h1 style="color: #e67e22;">About Me</h1>
            <p>My name is <strong>Mubarak</strong>.</p>
            <p>I am a full-stack web developer learning Django and building production-ready websites.</p>
            <p>Passionate about clean code and scalable solutions. 🚀</p>
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
            <h1 style="color: #27ae60;">Contact Me</h1>
            <p>Email: mubarak@djangolearner.com</p>
            <p>LinkedIn: linkedin.com/in/mubarak</p>
            <p>GitHub: github.com/mubarak</p>
            <p>Let's collaborate on your next project!</p>
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
            <h1 style="color: #e74c3c;">Technical Skills</h1>
            <ul style="list-style: none;">
                <li>🐍 Python 3.11+</li>
                <li>🌐 Django Framework</li>
                <li>💻 HTML & CSS</li>
                <li>🗄️ Database Design</li>
                <li>🔧 RESTful APIs</li>
                <li>📦 Git & Version Control</li>
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
            <h1 style="color: #8e44ad;">Featured Projects</h1>
            <p><strong>Project 1:</strong> Django Portfolio Website</p>
            <p style="font-size: 14px; color: #666;">A multi-page Django application showcasing full-stack capabilities</p>
            
            <p><strong>Project 2:</strong> Task Management App (In Development)</p>
            <p style="font-size: 14px; color: #666;">CRUD application with database integration and user authentication</p>
            
            <p><strong>Project 3:</strong> API Service (Coming Soon)</p>
            <p style="font-size: 14px; color: #666;">RESTful API with Django Rest Framework</p>
            
            <a href="/">← Back to Home</a>
        </body>
    </html>
    """
    return HttpResponse(html)

def hello(request, name):
#                  ↑
#         Django passes the URL parameter here automatically!
    html = f"""
    <html>
        <body style="font-family: Arial; text-align: center;
                     background-color: #f0f8ff; padding: 50px;">
            <h1 style="color: #2e86de;">👋 Hello, {name}!</h1>
            <p>Welcome to my Django website!</p>
            <p>Django caught your name right from the URL! 🎉</p>
            <a href="/">← Back to Home</a>
        </body>
    </html>
    """
    return HttpResponse(html)


def age(request, years):
    html = f"""
    <html>
        <body style="font-family: Arial; text-align: center;
                     background-color: #fff0f5; padding: 50px;">
            <h1 style="color: #e74c3c;">🎂 Age Calculator</h1>
            <p>You are <strong>{years}</strong> years old!</p>
            <p>That means you were born around 
               <strong>{2026 - years}</strong>!</p>
            <a href="/">← Back to Home</a>
        </body>
    </html>
    """
    return HttpResponse(html)
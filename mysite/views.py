from django.http import HttpResponse

def home(request):
    html = """
    <html>
        <body style="font-family: Arial; text-align: center; 
                     background-color: #f0f8ff; padding: 50px;">
            <h1 style="color: #2e86de;">🕌 Assalamu Alaikum!</h1>
            <h2>Welcome to My Django Website</h2>
            <p>I built this with <strong>Python</strong> 
               and <strong>Django 5.2</strong>!</p>
            <a href="/about/">Go to About Page →</a>
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
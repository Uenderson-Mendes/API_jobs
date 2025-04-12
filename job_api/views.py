# job_api/views.py
from django.http import HttpResponse

def api_root(request):
    html = """
    <html>
        <head>
            <title>Job Portal API</title>
            <style>
                body { font-family: Arial, sans-serif; padding: 40px; }
                h1 { color: #2c3e50; }
                ul { list-style-type: none; padding: 0; }
                li { margin: 10px 0; }
                a { text-decoration: none; color: #3498db; font-size: 18px; }
                a:hover { text-decoration: underline; }
            </style>
        </head>
        <body>
            <h1>Bem-vindo à API do Job Portal</h1>
            <p>Confira os endpoints disponíveis:</p>
            <ul>
                <li><a href="/api/users/">Users</a></li>
                <li><a href="/api/companies/">Companies</a></li>
                <li><a href="/api/jobs/">Jobs</a></li>
                <li><a href="/api/applications/">Applications</a></li>
                <li><a href="/api/messaging/">Messaging</a></li>
                <li><a href="/api-auth/login/">Login (DRF)</a></li>
                <li><a href="/api-auth/logout/">Logout (DRF)</a></li>
            </ul>
        </body>
    </html>
    """
    return HttpResponse(html)

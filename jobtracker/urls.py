from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.http import HttpResponse

from tracking.models import Company, Job, Application, Interview

def home(request):
    company_count = Company.objects.count()
    job_count = Job.objects.count()
    app_count = Application.objects.count()
    interview_count = Interview.objects.count()

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Job Application Tracker</title>
        <!-- Bootstrap CDN -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-light">
        <div class="container mt-5">
            <div class="card shadow-lg p-4 rounded">
                <h1 class="text-center text-primary mb-4">Job Application Tracker API</h1>
                <p class="text-center">A platform where recruiters manage jobs and applicants track their applications.</p>

                <h3 class="mt-4"> System Statistics</h3>
                <div class="row text-center mt-3">
                    <div class="col-md-3">
                        <div class="card bg-white shadow-sm p-3">
                            <h4>{company_count}</h4>
                            <p>Companies</p>
                        </div>
                    </div>
                    <div class="col-md-3">
                        <div class="card bg-white shadow-sm p-3">
                            <h4>{job_count}</h4>
                            <p>Jobs</p>
                        </div>
                    </div>
                    <div class="col-md-3">
                        <div class="card bg-white shadow-sm p-3">
                            <h4>{app_count}</h4>
                            <p>Applications</p>
                        </div>
                    </div>
                    <div class="col-md-3">
                        <div class="card bg-white shadow-sm p-3">
                            <h4>{interview_count}</h4>
                            <p>Interviews</p>
                        </div>
                    </div>
                </div>

                <h3 class="mt-4"> Quick Links</h3>
                <ul class="list-group">
                    <li class="list-group-item"><a href="/admin/">Admin Dashboard</a></li>
                    <li class="list-group-item"><a href="/api/">API Endpoints</a></li>
                </ul>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)


def health_check(request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path("", home),
    path('admin/', admin.site.urls),
    path('api/health/', health_check),
    path('api/', include('tracking.urls')),
]
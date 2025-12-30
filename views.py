from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Job, Application

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job list.html', {'jobs': jobs})

@login_required
def post_job(request):
    if request.method == 'POST':
        Job.objects.create(
            title=request.POST['title'],
            company=request.POST['company'],
            location=request.POST['location'],
            salary=request.POST['salary'],
            description=request.POST['description'],
            posted_by=request.user
        )
        return redirect('job_list')
    return render(request, 'jobs/post_job.html')

@login_required
def apply_job(request, job_id):
    job = Job.objects.get(id=job_id)
    if request.method == 'POST':
        Application.objects.create(
            job=job,
            applicant=request.user,
            resume=request.FILES['resume']
        )
        return redirect('job_list')
    return render(request, 'jobs/apply job.html', {'job': job})

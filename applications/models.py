from django.db import models

# Create your models here.

class ApplicationStatus(models.TextChoices):
    DRAFT = "Draft"
    SUBMITTED = "Submitted"
    INTERVIEW = "Interview"
    OFFER = "Offer"
    REJECTED = "Rejected"
    WITHDRAWN = "Withdrawn"

class JobApplication(models.Model):
    company_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    status = models.CharField(
        max_length=20,
        choices=ApplicationStatus.choices,
        default=ApplicationStatus.DRAFT,
    )
    company_website = models.URLField(blank=True)
    job_posting_url = models.URLField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    date_applied = models.DateField(blank=True)
    interview_date = models.DateTimeField(null=True,blank=True)
    notes = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.company_name} - {self.job_title}"

class Resume(models.Model):
    application = models.ForeignKey(
        JobApplication,
        on_delete=models.CASCADE,
        related_name="resumes",
    )
    file = models.FileField(upload_to="resumes/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resume for {self.application.company_name} - {self.application.job_title}"
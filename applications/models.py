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
    company_name = models.CharField(null=True, max_length=200)
    job_title = models.CharField(null=True, max_length=200)
    status = models.CharField(
        max_length=20,
        choices=ApplicationStatus.choices,
        default=ApplicationStatus.DRAFT,
    )
    job_posting_url = models.URLField(null=True, blank=True)
    company_website = models.URLField(null=True, blank=True)
    location = models.CharField(null=True, max_length=255, blank=True)
    date_applied = models.DateField(null=True, blank=True)
    interview_date = models.DateTimeField(null=True, blank=True)
    resume_file = models.FileField(null=True, upload_to="resumes/", blank=True)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.company_name} - {self.job_title} - {self.status}"

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
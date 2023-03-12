from django.db import models


# Create your models here.
class Victim(models.Model):
    name                = models.CharField(max_length=50, blank=True)
    current_position    = models.CharField(max_length=50, blank=True)
    location            = models.CharField(max_length=100, blank=True)
    about               = models.CharField(max_length=400, blank=True)
    positions           = models.CharField(max_length=400, blank=True)
    companies           = models.CharField(max_length=400, blank=True)
    durations           = models.CharField(max_length=400, blank=True)
    job_descriptions    = models.CharField(max_length=400, blank=True)
    institutions        = models.CharField(max_length=400, blank=True)
    tenures             = models.CharField(max_length=400, blank=True)
    victim_skills       = models.CharField(max_length=400, blank=True)
    github_repos        = models.CharField(max_length=400, blank=True)
    template_number     = models.CharField(max_length=1, blank=False, default="1")
    
class LinkedIn(models.Model):
    linkedin_url = models.CharField(max_length=100)
    github_url = models.CharField(max_length=100)
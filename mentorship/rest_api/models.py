from django.db import models

class Mentor(models.Model):
    GENDER_CHOICES = [('f', 'Female'), ('m', 'Male'), ('u', 'Undefined')]
    name = models.CharField(max_length=64)
    email = models.EmailField()
    gender = models.CharField(max_length=9, choices=GENDER_CHOICES, default='f')

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Mentorship(models.Model):
    STATUS_CHOICES = [('active', 'Active'), ('disabled', 'Disabled')]
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES,
                                                            default='active')
    def __str__(self):
        return f"{self.mentor} ({self.project.name})"

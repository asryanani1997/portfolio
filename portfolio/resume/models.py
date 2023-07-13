from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Skill(models.Model):
    name = models.TextField(max_length=30)
    value = models.PositiveIntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)], default=1)

    def __str__(self) -> str:
        return f"{self.name} skill value is {self.value}"


class Experience(models.Model):
    job_position = models.TextField()
    start_date = models.TimeField()
    end_date = models.TimeField()
    is_current = models.BooleanField()
    address = models.TextField()
    job_description = models.TextField()
    company_name = models.TextField()

    def __str__(self) -> str:
        return f"{self.company_name} company, job position is {self.job_position}"


class Education(models.Model):
    university_name = models.TextField()
    start_date = models.DateField()
    end_date = models.TimeField()
    degree = models.TextField(max_length=30, blank=True, null=True)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.university_name} university, degree is {self.degree}"

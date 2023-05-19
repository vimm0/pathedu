from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django import forms

User = get_user_model()

COUNTRY = (
    (1, 'USA'),
    (2, 'AUSTRAILIA'),
    (3, 'UNITED KINGDOM'),
    (4, 'CANADA'),
    (5, 'EUROPE'),
    (6, 'NEW ZEALAND'),
    (7, 'DUBAI'),
    (8, 'JAPAN'),
    (9, 'KOREA'),
    (10, 'INDIA'),
    (11, 'BANGLADESH'),
)

QUALIFICATION = (
    (1, 'SEE'),
    (2, '+2'),
    (3, 'DIPLOMA'),
    (4, 'BACHELORS'),
    (5, 'POST GRADUATE DIPLOMA'),
    (6, 'MASTERS'),
    (7, 'B. Nursing'),
    (8, 'PCL Nursing'),
)

PLATFORM = (
    (1, 'FACEBOOK'),
    (2, 'INSTAGRAM'),
    (3, 'OTHERS'),
)

class ModifiedArrayField(ArrayField):
    # https://rogulski.it/django-multiselect-choice-admin/
    def formfield(self, **kwargs):
        defaults = {
            "form_class": forms.MultipleChoiceField,
            "choices": self.base_field.choices,
            "widget": forms.CheckboxSelectMultiple,
            **kwargs
        }
        return super(ArrayField, self).formfield(**defaults)



class Applicant(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    qualification_upto = models.IntegerField(choices=QUALIFICATION, null=True, blank=True, help_text='Qualification done by student upto now.')
    # year, grade -> divison
    qualification_for = models.IntegerField(choices=QUALIFICATION, null=True, blank=True, help_text='Qualification for which student want to go abroad.')
    country_for = ModifiedArrayField(
        models.CharField(
            choices=COUNTRY,
            max_length=100,
            blank=True,
            null=True
        ),
        blank=True,
        null=True
    )

    counsellor = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class SocialMedia(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    platform = models.IntegerField(choices=PLATFORM, null=True, blank=True)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.link
    
class Qualification(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    level = models.IntegerField(choices=QUALIFICATION, null=True, blank=True)
    grade = models.CharField(max_length=255)

    def __str__(self):
        return self.applicant
    
class Query(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    question = models.TextField(max_length=255)
    answer = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.applicant
from django import forms
from django.contrib import admin
from apps.core.models import Applicant, SocialMedia, Qualification, Query

class SocialMediaInlineAdmin(admin.TabularInline):
    model = SocialMedia
    extra = 0

class QualificationInlineAdmin(admin.TabularInline):
    model = Qualification
    extra = 0
    after_field = "phone"

class QueryInlineAdmin(admin.TabularInline):
    model = Query
    extra = 0


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    fields = (
        'name',
        ('phone', 'email',),
        'address',
        ('qualification_upto', 'qualification_for'),
        'country_for',
    )
    inlines = [
        QualificationInlineAdmin,
        QueryInlineAdmin,
        SocialMediaInlineAdmin,
    ]
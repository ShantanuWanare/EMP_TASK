from .models import EmpQualification
from .models import EmpWorkExperience
from .models import EmpAddressDetails
from .models import EmpPersonalDetails
from .models import EmpProjects
from django.contrib import admin


@admin.register(EmpPersonalDetails)
class EmpPersonalDetailsAdmin(admin.ModelAdmin):
    list_display = ('regid', 'name', 'email', 'age', 'gender', 'phoneNo', 'photo')


@admin.register(EmpAddressDetails)
class EmpAddressDetailsAdmin(admin.ModelAdmin):
    list_display = ('emp', 'hno', 'street', 'city', 'state', )


@admin.register(EmpWorkExperience)
class EmpWorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('emp', 'companyName', 'fromDate', 'toDate', 'address', )


@admin.register(EmpQualification)
class EmpQualificationAdmin(admin.ModelAdmin):
    list_display = ('emp', 'qualificationName', 'percentage', )


@admin.register(EmpProjects)
class EmpProjectsAdmin(admin.ModelAdmin):
    list_display = ('emp', 'title', 'description', )


from django.db import models

class EmpPersonalDetails(models.Model):
    def nameFile(instance, filename):
        return '/'.join(['images', str(instance.name),filename])
    regid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    phoneNo = models.CharField(max_length=10)
    photo = models.ImageField(upload_to=nameFile, blank=True)

    def __str__(self):
        return f'{self.regid}'



class EmpAddressDetails(models.Model):
    emp = models.OneToOneField(
        EmpPersonalDetails, on_delete=models.CASCADE,  related_name='EmpAddressDetails')
    hno = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.emp.regid}'


class EmpWorkExperience(models.Model):
    emp = models.ForeignKey(
        EmpPersonalDetails, on_delete=models.CASCADE,  related_name='EmpWorkExperience')
    companyName = models.CharField(max_length=100)
    fromDate = models.CharField(max_length=100)
    toDate = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.emp.regid}'


class EmpQualification(models.Model):
    emp = models.ForeignKey(
        EmpPersonalDetails, on_delete=models.CASCADE,  related_name='EmpQualification')
    qualificationName = models.CharField(max_length=100)
    percentage = models.FloatField()

    def __str__(self):
        return f'{self.emp.regid}'


class EmpProjects(models.Model):
    emp = models.ForeignKey(
        EmpPersonalDetails, on_delete=models.CASCADE,  related_name='EmpProjects')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.emp.regid}'





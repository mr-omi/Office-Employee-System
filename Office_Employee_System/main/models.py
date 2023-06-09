from django.db import models


class department(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class employee(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(department, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    salary = models.IntegerField()
    bonus = models.IntegerField()
    phone = models.IntegerField()
    hire_date = models.DateField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

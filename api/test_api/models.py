from django.db import models

# Create your models here.

class Test_form(models.Model):

    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.first_name, self.email)

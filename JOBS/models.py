from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to="images/")  # folder inside which the images uploaded by user should be placed
    describe_image = models.CharField(max_length=200)  # fix the no. of text in description of image.
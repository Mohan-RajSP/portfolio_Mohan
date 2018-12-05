from django.db import models



class BlogModel(models.Model):
    Tittle = models.CharField(max_length=255)
    Content = models.TextField()
    Image = models.ImageField(upload_to="images/")
    Date = models.DateField()

    def summary(self):
        return (self.Content[:100] + "...")

    def __str__(self):
        return (self.Tittle)





# Create your models here.

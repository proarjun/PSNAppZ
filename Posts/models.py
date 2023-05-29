from django.db import models

# Create your models here.
class Posts(models.Model):
    caption = models.CharField(max_length=50)
    description = models.CharField(max_length=2500)
    tags = models.CharField(max_length=100)
    created_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='mediafiles', blank=True, null=True)

    def __str__(self) -> str:
        return self.caption


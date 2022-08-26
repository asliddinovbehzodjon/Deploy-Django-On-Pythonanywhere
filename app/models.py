from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=5000,verbose_name="Post Nomi",help_text="Post uchun sarlavha kiriting")
    image = models.ImageField(upload_to ='post-images',verbose_name="Post Rasmi",help_text="Post uchun rasm kiriting")
    def __str__(self):
        return self.name
    
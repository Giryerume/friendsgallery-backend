from django.db import models

# Create your models here.
class Photo(models.Model):
    user=models.ForeignKey('auth.User', related_name='photos', on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    comment=models.CharField(max_length=1000)
    image=models.ImageField(upload_to='image')
    date=models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

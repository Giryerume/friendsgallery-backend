from django.db import models
from photos.models import Photo


# Create your models here.
class Approve(models.Model):
    photo=models.ForeignKey(Photo, related_name='approve', on_delete=models.CASCADE)
    user=models.ForeignKey('auth.user', related_name='approved_by', on_delete=models.CASCADE, default=None, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.photo.title
